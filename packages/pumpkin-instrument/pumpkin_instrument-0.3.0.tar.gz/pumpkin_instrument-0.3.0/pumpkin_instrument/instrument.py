"""
General implementation of an instrument
"""
from abc import abstractmethod
from typing import List, ContextManager, Any
try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

from .types import InstrumentType


class Instrument(Protocol):
    """
    Base class for instruments
    """
    @classmethod
    @abstractmethod
    def instrument_type(cls) -> InstrumentType:
        """
        What type of pumpkin_instrument is implemented. Currently there is:
            - PowerSupply
            - Load
            - Multimeter
            - Thermocouple
            - PressureGauge
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def instrument_capabilities(cls) -> Any:
        """
        Describes the capabilities of the pumpkin_instrument that apply to all channels. Currently this is only a placeholder
        for future API expansion.
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def channel_capabilities(cls) -> List[Any]:
        """
        Describes channel capabilities
        """
        raise NotImplementedError()

    @abstractmethod
    def use(self) -> ContextManager[Any]:
        """
        Uses the pumpkin_instrument, taking control of it.

        This will automatically close the instrument after exiting the context manager allowing cleanup of outputs/inputs.
        """
        raise NotImplementedError()
