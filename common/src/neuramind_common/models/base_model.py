from abc import ABC, abstractmethod

from openai import AzureOpenAI

from neuramind_common.config import config


class BaseModel(ABC):
    type: str
    db_node_name: str
    tenant_id: str
    source: str

    def __init__(self, type: str, db_node_name: str, tenant_id: str, source: str):
        self.type = type
        self.db_node_name = db_node_name
        self.tenant_id = tenant_id
        self.source = source

    @abstractmethod
    def get_embedding_text(self) -> str:
        pass

    @staticmethod
    def get_embeddings(items: list["BaseModel"]) -> list[str]:
        azure_open_ai_client = AzureOpenAI(
            azure_endpoint=config.azure_openai_endpoint,
            api_key=config.azure_openai_api_key,
            api_version="2024-06-01",
        )
        item_embedding_texts = []
        for x_item in items:
            item_embedding_texts.append(x_item.get_embedding_text())
        embedding_response = azure_open_ai_client.embeddings.create(
            input=item_embedding_texts, model="text-embedding-3-large"
        )
        embeddings = []
        for data in embedding_response.data:
            embeddings.append(data.embedding)
        return embeddings

    @staticmethod
    @abstractmethod
    def to_db_dict(items: "BaseModel") -> dict:
        pass
