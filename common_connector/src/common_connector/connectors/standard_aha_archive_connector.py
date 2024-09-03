from neuramind_common import AhaArchivEntryModel

from .base_connector import BaseConnector


class StandardAhaArchiveConnector(BaseConnector[AhaArchivEntryModel]):
    def __init__(self):
        super().__init__()

    def load(self) -> list[AhaArchivEntryModel]:
        # load the aha archive entries from firebase, based on phase (LIVESTAGE, PLAYGROUND, TESTBENCH)
        test_aha_archive_entry_models = [
            AhaArchivEntryModel(
                tenant_id="test",
                source="test",
                title="test",
                description="test",
                url="test",
            )
        ]
        return test_aha_archive_entry_models
