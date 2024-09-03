from common_connector.connectors.base_connector import BaseConnector


class BaseConnectorManager:
    def __init__(self, tenant_id: str, connectors: list[BaseConnector]):
        self.tenant_id = tenant_id
        self.connectors = connectors

    def connect_all(self):
        for connector in self.connectors:
            connector.connect(self.tenant_id)
