FROM python:3.7-alpine

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
CMD ["sh"]