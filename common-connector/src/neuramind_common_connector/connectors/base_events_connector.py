from abc import ABC, abstractmethod

from neuramind_common.models.event_model import EventModel

from .base_connector import BaseConnector


class BaseEventsConnector(ABC, BaseConnector[EventModel]):
    def __init__(self, tenant_id: str):
        super().__init__(tenant_id)

    @abstractmethod
    def load(self) -> list[EventModel]:
        pass

    @abstractmethod
    def upload(self, items: list[EventModel]):
        pass
