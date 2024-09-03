from .base_model import BaseModel


class BaseUnstructuredModel(BaseModel):
    text: str

    def __init__(
        self, type: str, db_node_name: str, tenant_id: str, source: str, text: str
    ):
        super().__init__(type, db_node_name, tenant_id, source)
        self.text = text

    def get_embedding_text(self) -> str:
        return self.text

    @staticmethod
    def to_db_dict(items: list["BaseUnstructuredModel"]) -> list[dict]:
        embeddings = BaseUnstructuredModel.get_embeddings(items)
        aha_archive_entry_db_dicts = []
        for x_item, x_embedding in zip(items, embeddings):
            aha_archive_entry_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "text": x_item.text,
                    "embedding": x_embedding,
                }
            )
        return aha_archive_entry_db_dicts
