from abc import ABC, abstractmethod

from common.models.base_model import BaseModel


class BaseUploader(ABC):
    @abstractmethod
    def upload(self, items: list[BaseModel]) -> None:
        pass
