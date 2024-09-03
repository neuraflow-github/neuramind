from datetime import datetime

from .base_model import BaseModel


class AhaArchivEntryModel(BaseModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        text: str,
    ):
        super().__init__("AhaArchivEntryModel", "AhaArchivEntry", tenant_id, source)
        self.text = text

    def get_embedding_text(self) -> str:
        return self.text

    @staticmethod
    def to_db_dict(items: list["AhaArchivEntryModel"]) -> list[dict]:
        aha_archiv_entry_db_dicts = []
        for x_item in items:
            aha_archiv_entry_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "text": x_item.text,
                    "embedding": "TODO",
                }
            )
        return aha_archiv_entry_db_dicts
