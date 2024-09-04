from datetime import datetime

from .base_model import BaseModel


class TestModel(BaseModel):
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
