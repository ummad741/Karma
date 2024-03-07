FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /fassite
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

RUN chmod a+x docker/*.sh
