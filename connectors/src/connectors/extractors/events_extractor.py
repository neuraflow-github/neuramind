from common.models.event_model import EventModel

from .base_extractor import BaseExtractor


class EventsExtractor(BaseExtractor[EventModel]):
    def __init__(self):
        super().__init__()

    def extract(self) -> list[EventModel]:
        pass
