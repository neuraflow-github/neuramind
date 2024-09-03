from abc import ABC, abstractmethod

from neuramind_common import EventModel

from .base_connector import BaseConnector


class BaseEventsConnector(ABC, BaseConnector[EventModel]):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def load(self) -> list[EventModel]:
        pass

    @abstractmethod
    def upload(self, items: list[EventModel]):
        pass
