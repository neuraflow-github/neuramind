from .base_model import BaseModel


class ServiceModel(BaseModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        name: str,
        description: str,
        price: int,
    ):
        super().__init__("ServiceModel", "Service", tenant_id, source)
        self.name = name
        self.description = description
        self.price = price

    def get_embedding_text(self) -> str:
        return f"{self.name}\n\n{self.description}"

    @staticmethod
    def to_db_dict(items: list["ServiceModel"]) -> list[dict]:
        service_db_dicts = []
        for x_item in items:
            service_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "name": x_item.name,
                    "description": x_item.description,
                    "price": x_item.price,
                    "embedding": "TODO",
                }
            )
        return service_db_dicts
