from abc import ABC, abstractmethod

from neuramind_common.models.press_release_model import PressReleaseModel

from .base_connector import BaseConnector


class BasePressReleasesConnector(ABC, BaseConnector[PressReleaseModel]):
    def __init__(self, tenant_id: str):
        super().__init__(tenant_id)

    @abstractmethod
    def load(self) -> list[PressReleaseModel]:
        pass

    @abstractmethod
    def upload(self, items: list[PressReleaseModel]):
        pass
