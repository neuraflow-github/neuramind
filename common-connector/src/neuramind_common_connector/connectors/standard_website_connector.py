from neuramind_common.models.website_chunk_model import WebsiteChunkModel

from .base_connector import BaseConnector


class StandardWebsiteConnector(BaseConnector[WebsiteChunkModel]):
    url: str
    ignore_globs: list[str]

    def __init__(self, tenant_id: str, url: str, ignore_globs: list[str]):
        super().__init__(tenant_id)
        self.url = url
        self.ignore_globs = ignore_globs

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
