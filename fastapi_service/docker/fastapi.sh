#!/bin/bash

echo "fastapi is started"

cd app

gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8050
