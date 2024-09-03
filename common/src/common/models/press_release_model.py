from datetime import datetime

from .base_model import BaseModel


class PressReleaseModel(BaseModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        title: str,
        content: str,
        published_at: datetime,
    ):
        super().__init__("PressReleaseModel", "PressRelease", tenant_id, source)
        self.title = title
        self.content = content
        self.published_at = published_at

    def get_embedding_text(self) -> str:
        return f"{self.title}\n\n{self.content}"

    @staticmethod
    def to_db_dict(items: list["PressReleaseModel"]) -> list[dict]:
        press_release_db_dicts = []
        for x_item in items:
            press_release_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "title": x_item.title,
                    "content": x_item.content,
                    "published_at": x_item.published_at,
                    "embedding": "TODO",
                }
            )
        return press_release_db_dicts
