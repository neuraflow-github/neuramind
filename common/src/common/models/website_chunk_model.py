from .base_model import BaseModel


class WebsiteChunkModel(BaseModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        text: str,
    ):
        super().__init__("WebsiteChunkModel", "WebsiteChunk", tenant_id, source)
        self.text = text

    def get_embedding_text(self) -> str:
        return self.text

    @staticmethod
    def to_db_dict(items: list["WebsiteChunkModel"]) -> list[dict]:
        embeddings = WebsiteChunkModel.get_embeddings(items)
        website_chunk_db_dicts = []
        for x_item, x_embedding in zip(items, embeddings):
            website_chunk_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "text": x_item.text,
                    "embedding": x_embedding,
                }
            )
        return website_chunk_db_dicts
