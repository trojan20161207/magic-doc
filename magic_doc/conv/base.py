
from abc import ABC, abstractmethod

from magic_doc.progress.pupdator import ConvProgressUpdator

class BaseConv(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def to_md(self, bits: bytes | str, pupdator:ConvProgressUpdator) -> str:
        return NotImplemented

    def to_mid_result(self, bits: bytes | str, pupdator:ConvProgressUpdator) -> list[dict] | dict:
        pupdator.update(100)
        return {}
