from typing import Optional

from neuramind_common.services.firebase import firebase


class AssistantsService:
    @staticmethod
    async def get_all() -> list[dict]:
        try:
            assistants_collection_ref = firebase.db.collection("assistants")
            assistant_docs = assistants_collection_ref.stream()
            assistants = []
            for x_assistant_doc in assistant_docs:
                assistants.append(x_assistant_doc.to_dict())
            return assistants
        except Exception as e:
            raise Exception(f"Failed getting assistants: {str(e)}")

    @staticmethod
    async def get(tenant_id: str) -> Optional[dict]:
        try:
            assistant_doc_ref = firebase.db.collection("assistants").document(tenant_id)
            assistant_doc = assistant_doc_ref.get()
            if not assistant_doc.exists:
                raise Exception("ASSISTANT_NOT_FOUND")
            assistant_data = assistant_doc.to_dict()
            return assistant_data
        except Exception as error:
            raise Exception(f"Failed getting assistant: {str(error)}")
