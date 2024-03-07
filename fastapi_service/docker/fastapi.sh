#!/bin/bash

echo "fastapi is started"

# alembic upgrade head

cd src

uvicorn main:app --host 0.0.0.0 --port 8055 --reload

# this code can't reload app 
# gunicorn -b 0.0.0.0:8050 -w 4 -k uvicorn.workers.UvicornWorker main:app --reload
