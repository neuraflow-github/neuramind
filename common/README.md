# Common

- Git trigger: 100

- gcloud artifacts repositories create python-main --location=europe-west3 --repository-format=python
- poetry config repositories.google <https://europe-west3-python.pkg.dev/chat-link-development/neuramind-common/simple/>
- poetry build
- poetry publish -r google
- poetry self update && poetry self add keyrings.google-artifactregistry-auth
- gcloud auth print-access-token |keyring set poetry-repository-neuramind oauth2accesstoken
