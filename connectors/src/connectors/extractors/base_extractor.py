from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from common.models.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseExtractor(ABC, Generic[T]):
    def __init__(self):
        pass

    @abstractmethod
    def extract(self) -> list[T]:
        pass
