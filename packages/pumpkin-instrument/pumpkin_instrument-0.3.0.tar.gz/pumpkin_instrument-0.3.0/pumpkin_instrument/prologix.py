"""
Implements prologix controllers for instruments
"""
# coding: utf-8
import socket
import time
from datetime import datetime
from enum import Enum
from select import select
from pathlib import Path
from itertools import repeat

from serial import Serial

PROLOGIX_BAUD = 9600
PROLOGIX_PORT = 1234


class PrologixType(Enum):
    """
    Supports Ethernet or USB prologix controllers (or test output)
    """
    Ethernet = 1
    USB = 2
    # `Test` will write the equivalent Prologix commands to a file
    # for testing purposes.
    Test = 3


def append_to_file(path: Path, data: bytes):
    """
    Appends the data to the file.
    Used for testing the Prologix controller and resources w/o access to a real controller.

    :param path: The file path to append to
    :param data: The bytes to write to the file
    """
    with path.open('ab') as f:
        f.write(data)


def read_poll_socket(sock: socket.socket, amount: int) -> bytes:
    """
    Reads the socket by polling it via select call, returning bytes if anything was read from the socket.

    :param sock: The socket to read the bytes from.
    :param amount: The amount of bytes to read from the socket
    :return: 0 or more bytes read from the socket.
    """
    readable, _, _ = select([sock], [], [], 0)
    if readable:
        return sock.recv(amount)
    return bytes()


class PrologixController:
    """Abstraction of the Prologix GP-IB controller. Handles both the Ethernet and USB controllers."""

    def __init__(self, controller_type: PrologixType, controller_address: str):
        """
        Opens the communication to the Prologix GP-IB controller via the specified `controller_type` and
        `controller_address`.

        `controller_address` is a COM|/dev/ttyUSB* port if type is USB, else it is an IP address.

        :param controller_type: The type of controller, either Ethernet or USB.
        :param controller_address: The device path or IP address of Prologix controller.
        """
        if controller_type == PrologixType.Ethernet:
            self._sock = socket.create_connection(
                (controller_address, PROLOGIX_PORT))
            self._sock.setblocking(True)  # Make the socket blocking.
            self.timeout = 200
            self._write = self._sock.sendall
            self._read = lambda amt: read_poll_socket(self._sock, amt)
            self._write(f'++read_tmo_ms {self.timeout}'.encode('ascii'))
        elif controller_type == PrologixType.USB:
            self._ser = Serial(controller_address, PROLOGIX_BAUD)
            self._ser.timeout = 0  # Make the serial socket non-blocking.
            self._write = self._ser.write
            self._read = self._ser.read
        elif controller_type == PrologixType.Test:
            # Test configuration to verify proper output of GPIB commands and
            # PSU/Load commands.
            self._file = Path(controller_address)
            # Write quick header
            with self._file.open('w') as f:
                f.write(f"--- {datetime.now().isoformat()} ---\n")
            self._write = lambda data: append_to_file(self._file, data)
            self._read = lambda amt: bytes(repeat(0, amt))
        else:
            raise ValueError(f'Unsupported controller type {controller_type}')
        self._curr_address = -1
        self._controller_type = controller_type
        self._write('++auto 0\n'.encode('ascii'))

    def _write_address(self, address):
        """
        Checks the currently addressed GPIB pumpkin_instrument and changes the device addressed by the Prologix
        controller if the current address does not match the requested `address`.

        :param address: The address to talk to on the GPIB bus.
        """
        if self._curr_address != address:
            self._write(f'++addr {address}\n'.encode('ascii'))
            self._curr_address = address

    @property
    def controller_type(self) -> PrologixType:
        """
        Gets the currently used prologix configuration type.

        :return: The type of prologix controller in use.
        """
        return self._controller_type

    def write(self, address: int, data: bytes):
        """
        Writes out the binary data to the address on the Prologix controller. Automatically switches the address the
        prologix controller is talking to if the previous address used is different.

        :param address: The address to write the data to.
        :param data: The binary data to write out to the controller.
        """
        self._write_address(address)
        self._write(data)

    def read(self, address: int, amount: int) -> bytes:
        """
        Reads binary data from the prologix GPIB controller. Automatically switches the address the
        prologix controller is talking to if the previous address used is different.

        :param address: The GPIB address to read from.
        :param amount: The amount of bytes to read from the prologix controller.
        :return: The bytes read from the prologix controller.
        """
        self._write_address(address)

        # Instruct pumpkin_instrument to talky talky and read back until EOI is
        # asserted.
        self._write('++read eoi\n'.encode('ascii'))
        return self._read(amount)

    def read_until(self, address: int, terminator: bytes = '\n'.encode(
            'ascii'), timeout: float = 0.5) -> bytes:
        """
        Reads from the pumpkin_instrument until a terminator is asserted. This will raise a RuntimeError if the terminator
        is not found after retrying 10 times.

        :param address: The address of the GPIB pumpkin_instrument to read from.
        :param terminator: The terminator bytes to search for in the response.
        :param timeout: The period of time, in seconds, to wait before giving up on a read.
        :return: The bytes of the response including the terminator.
        """
        # constants local to the method
        sleep_time = 0.05
        block_size = 64

        # Instruct the pumpkin_instrument to talky talky and read back until
        # EOI is asserted.
        self.write(address, '++read eoi\n'.encode('ascii'))
        response = bytearray()
        end_time = time.time() + 0.5
        while True:
            b = self._read(block_size)

            # Check to see if we got something from the GPIB bus, if not, fail after we pass the end_time of the timeout
            # period
            if not b:
                if time.time() > end_time:
                    raise RuntimeError(
                        f'Instrument failed to respond with {terminator} bytes terminator.')
                time.sleep(sleep_time)
                continue

            response += b
            try:
                # Check for the terminator in the response.
                response.index(terminator)
                break
            except ValueError:
                # Terminator not found, we're good to continue.
                pass

        return bytes(response)

    def selected_device_clear(self, address: int):
        """Sends the ++clr command to clear the output/input buffer of the instruments to get it back on track"""
        # Now read off until we get anything, but ignore the errors
        try:
            self.read_until(address)
        except BaseException:
            pass
        self._write('++clr\n'.encode('ascii'))
        time.sleep(0.5)  # Wait a bit for the instrument to clear its stuff up.
