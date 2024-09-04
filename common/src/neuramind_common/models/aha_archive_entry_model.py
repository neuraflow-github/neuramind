from .base_unstructured_model import BaseUnstructuredModel


class AhaArchiveEntryModel(BaseUnstructuredModel):
    def __init__(
        self,
        tenant_id: str,
        source: str,
        text: str,
    ):
        super().__init__(
            "AhaArchiveEntryModel", "AhaArchiveEntry", tenant_id, source, text
        )
