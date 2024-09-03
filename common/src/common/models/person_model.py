from typing import Optional

from .base_model import BaseModel


class PersonModel(BaseModel):
    full_name: str
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    email_address: Optional[str] = None
    address: Optional[str] = None
    room: Optional[str] = None

    def __init__(
        self,
        tenant_id: str,
        source: str,
        full_name: str,
        gender: str = None,
        phone_number: Optional[str] = None,
        email_address: Optional[str] = None,
        address: Optional[str] = None,
        room: Optional[str] = None,
    ):
        super().__init__("PersonModel", "Person", tenant_id, source)
        self.full_name = full_name
        self.gender = gender
        self.phone_number = phone_number
        self.email_address = email_address
        self.address = address
        self.room = room

    def get_embedding_text(self) -> str:
        return f"{self.full_name} {self.gender or ''} {self.email_address or ''} {self.address or ''} {self.room or ''}"

    @staticmethod
    def to_db_dict(items: list["PersonModel"]) -> list[dict]:
        embeddings = PersonModel.get_embeddings(items)
        person_db_dicts = []
        for x_item, x_embedding in zip(items, embeddings):
            person_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "full_name": x_item.full_name,
                    "gender": x_item.gender,
                    "phone_number": x_item.phone_number,
                    "email_address": x_item.email_address,
                    "address": x_item.address,
                    "room": x_item.room,
                    "embedding": x_embedding,
                }
            )
        return person_db_dicts
