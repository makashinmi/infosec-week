FROM python:3.12.7

WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir --upgrade sqlalchemy "fastapi[standard]" alembic

COPY . /backend 

EXPOSE 8000
CMD ["fastapi", "run", "/backend/wsgi.py"]
