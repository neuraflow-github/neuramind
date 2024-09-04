import importlib.util
import os

from fastapi import FastAPI, HTTPException
from neuramind_common.enums.phase import Phase
from neuramind_common.services.assistants_service import AssistantsService
from neuramind_connector_api.config import config

app = FastAPI()


@app.post("/connect_outdated_tenants")
async def connect_outdated_tenants():
    # This endpoint is left empty for now
    # get all assistants from firebase and check the last time the assistant was connected
    # sort them by the last time they were connected
    # connect top 5
    pass


@app.post("/connect_tenant")
async def connect_tenant(tenant_id: str, phase: Phase):
    # Get the assistant by tenant id from firebase
    assistant = await AssistantsService.get(tenant_id)

    # Get the folder with the connector code
    if phase == Phase.TESTBENCH:
        base_path = os.environ.get("TESTBENCH_CUSTOM_CONNECTORS_PATH")
    elif phase in [Phase.PLAYGROUND, Phase.LIVESTAGE]:
        base_path = f"custom-connectors/{phase.lower()}"
    else:
        raise HTTPException(status_code=400, detail=f"Invalid phase: {phase}")

    # Get the subfolder for the specific tenant
    tenant_folder = None
    for folder in os.listdir(base_path):
        if folder.endswith(f"|{tenant_id}"):
            tenant_folder = folder
            break
    if not tenant_folder:
        raise HTTPException(
            status_code=404, detail=f"Tenant folder not found for {tenant_id}"
        )

    full_path = os.path.join(base_path, tenant_folder)

    # Load the custom_connection_manager.py
    spec = importlib.util.spec_from_file_location(
        "custom_connection_manager",
        os.path.join(full_path, "custom_connection_manager.py"),
    )
    custom_connection_manager = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(custom_connection_manager)

    # Call the connect_all method
    try:
        custom_connection_manager.connect_all()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during connection: {str(e)}"
        )

    return {"message": "Connection completed successfully"}


if __name__ == "__main__":
    # Dev mode needs 127.0.0.1. GCP Cloud Run needs 0.0.0.0
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=config.port, reload=True)
