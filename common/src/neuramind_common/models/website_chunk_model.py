from .base_model import BaseModel


class WebsiteChunkModel(BaseModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        text: str,
    ):
        super().__init__("WebsiteChunkModel", "WebsiteChunk", tenant_id, source, text)
