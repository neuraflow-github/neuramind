from .base_unstructured_model import BaseUnstructuredModel


class WebsiteChunkModel(BaseUnstructuredModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        text: str,
    ):
        super().__init__("WebsiteChunkModel", "WebsiteChunk", tenant_id, source, text)
