import os
from abc import ABC, abstractmethod

from openai import AzureOpenAI


class BaseModel(ABC):
    def __init__(self, type: str, db_node_name: str, tenant_id: str, source: str):
        self.type = type
        self.db_node_name = db_node_name
        self.tenant_id = tenant_id
        self.source = source

    @abstractmethod
    def get_embedding_text(self) -> str:
        pass

    @staticmethod
    def get_embedding_text_list(items: list["BaseModel"]) -> list[str]:

        client = AzureOpenAI(
            api_key=config.,
            api_version="2024-06-01",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        )

        texts = [x_item.get_embedding_text() for x_item in items]

        embeddings = []

        for text in texts:
            response = client.embeddings.create(
                input=text, model="text-embedding-3-large"
            )
            embeddings.append(response.data[0].embedding)

        return embeddings

    @staticmethod
    @abstractmethod
    def to_db_dict(items: "BaseModel") -> dict:
        pass
