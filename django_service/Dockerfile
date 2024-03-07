FROM python:3.10

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /djansite
COPY requirements.txt /djansite/requirements.txt
RUN pip install -r requirements.txt
COPY . /djansite/

RUN chmod a+x docker/*.sh