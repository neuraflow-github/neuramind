# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim-stretch
# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY app .
# Install dependencies.
RUN pip install -r requirements.txt
# Run your server
CMD exec pserve server.ini
