from datetime import datetime

from .base_model import BaseModel


class EventModel(BaseModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        title: str,
        description: str,
        start_at: datetime,
        end_at: datetime,
    ):
        super().__init__("EventModel", "Event", tenant_id, source)
        self.title = title
        self.description = description
        self.start_at = start_at
        self.end_at = end_at

    def get_embedding_text(self) -> str:
        return "\n".join(
            filter(
                None,
                [
                    self.title,
                    self.description,
                ],
            )
        )

    @staticmethod
    def to_db_dict(items: list["EventModel"]) -> list[dict]:
        embeddings = EventModel.get_embeddings(items)
        event_db_dicts = []
        for x_item, x_embedding in zip(items, embeddings):
            event_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "title": x_item.title,
                    "description": x_item.description,
                    "start_at": x_item.start_at,
                    "end_at": x_item.end_at,
                    "embedding": x_embedding,
                }
            )
        return event_db_dicts
