from neuramind_common.models.aha_archive_entry_model import AhaArchiveEntryModel

from .base_connector import BaseConnector


class StandardAhaArchiveConnector(BaseConnector[AhaArchiveEntryModel]):
    def __init__(self, tenant_id: str):
        super().__init__(tenant_id)

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
