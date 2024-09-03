from neuramind_common import AhaArchiveEntryModel

from .base_connector import BaseConnector


class StandardAhaArchiveeConnector(BaseConnector[AhaArchiveEntryModel]):
    def __init__(self):
        super().__init__()

    def load(self) -> list[AhaArchiveEntryModel]:
        # load the aha archive entries from firebase, based on phase (LIVESTAGE, PLAYGROUND, TESTBENCH)
        test_aha_archivee_entry_models = [
            AhaArchiveEntryModel(
                tenant_id="test",
                source="test",
                title="test",
                description="test",
                url="test",
            )
        ]
        return test_aha_archivee_entry_models
