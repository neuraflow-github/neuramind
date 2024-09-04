from neuramind_common.models.event_model import EventModel

from .base_events_connector import BaseEventsConnector


class StandardDrupalEventsConnector(BaseEventsConnector):
    def __init__(self):
        super().__init__()

    def load(self) -> list[EventModel]:
        # load the events from Drupal API
        test_event_models = [
            EventModel(
                tenant_id="test",
                source="drupal",
                title="Test Event",
                description="This is a test event",
                start_date="2023-01-01",
                end_date="2023-01-02",
                location="Test Location",
                url="https://test-event.com",
            )
        ]
        return test_event_models
