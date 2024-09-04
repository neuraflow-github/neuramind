from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from neuramind_common.models.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)


class BaseConnector(ABC, Generic[T]):
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id

    @abstractmethod
    def load(self) -> list[T]:
        pass

    @abstractmethod
    def upload(self, items: list[T]):
        # connect to neo 4j by db session object
        # upload nodes to neo 4j
        # upload relationships to neo 4j
        pass

    def connect(self):
        items = self.load()
        self.upload(items)
