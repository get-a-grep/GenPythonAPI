FROM python:latest

WORKDIR /code

COPY ./genapi/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./genapi /code/genapi

WORKDIR /code/genapi

ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]