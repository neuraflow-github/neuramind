from typing import Optional

from .base_model import BaseModel


class OrganizationModel(BaseModel):
    name: str
    address: Optional[str] = None

    def __init__(
        self,
        tenant_id: str,
        source: str,
        name: str,
        address: Optional[str] = None,
    ):
        super().__init__("OrganizationModel", "Organization", tenant_id, source)
        self.name = name
        self.address = address

    def get_embedding_text(self) -> str:
        return f"{self.name}\n\n{self.address}"

    @staticmethod
    def to_db_dict(items: list["OrganizationModel"]) -> list[dict]:
        embeddings = OrganizationModel.get_embeddings(items)
        organization_db_dicts = []
        for x_item, x_embedding in zip(items, embeddings):
            organization_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "name": x_item.name,
                    "address": x_item.address,
                    "embedding": x_embedding,
                }
            )
        return organization_db_dicts
