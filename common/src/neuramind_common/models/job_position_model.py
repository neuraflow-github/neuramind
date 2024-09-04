from datetime import datetime
from typing import Optional

from .base_model import BaseModel


class JobPositionModel(BaseModel):
    title: str
    description: str
    requirements: str
    responsibilities: str
    location: str
    employment_type: str
    salary: int
    application_deadline: datetime

    def __init__(
        self,
        tenant_id: str,
        source: str,
        name: str,
        address: Optional[str] = None,
    ):
        super().__init__("JobPositionModel", "JobPosition", tenant_id, source)
        self.name = name
        self.address = address

    def get_embedding_text(self) -> str:
        return "\n".join(
            filter(
                None,
                [
                    self.title,
                    self.description,
                    self.requirements,
                    self.responsibilities,
                    self.location,
                    self.employment_type,
                    str(self.salary),
                    self.application_deadline.isoformat(),
                ],
            )
        )

    @staticmethod
    def to_db_dict(items: list["JobPositionModel"]) -> list[dict]:
        embeddings = JobPositionModel.get_embeddings(items)
        job_position_db_dicts = []
        for x_item, x_embedding in zip(items, embeddings):
            job_position_db_dicts.append(
                {
                    "tenant_id": x_item.tenant_id,
                    "source": x_item.source,
                    "name": x_item.name,
                    "address": x_item.address,
                    "embedding": x_embedding,
                }
            )
        return job_position_db_dicts
