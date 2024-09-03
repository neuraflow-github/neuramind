from common.models.website_chunk_model import WebsiteChunkModel

from .base_loader import BaseExtractor


class WebsiteChunksExtractor(BaseExtractor[WebsiteChunkModel]):
    def __init__(self):
        super().__init__()

    def extract(self) -> list[WebsiteChunkModel]:
        pass
