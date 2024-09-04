from neuramind_common.models.website_chunk_model import WebsiteChunkModel

from .base_connector import BaseConnector


class StandardWebsiteChunksConnector(BaseConnector[WebsiteChunkModel]):
    def __init__(self):
        super().__init__()

    def load(self) -> list[WebsiteChunkModel]:
        # load the website chunks via apify
        test_data = [
            WebsiteChunkModel(
                tenant_id="test",
                source="test",
                title="test",
                description="test",
                url="test",
            )
        ]
        return test_data
