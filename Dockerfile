FROM python:3.13.5-slim-bullseye

WORKDIR /devtrack

COPY . /devtrack

RUN pip3 install -r /devtrack/requirments.txt

ENV DATABASE="postgresql://postgres:example@postgres:5432/devtrack" \
    SECRET="51ecfcb4e78f1984a8f3cbc8893aba613cf0b3ed5a84416439f289e019cf7003" \
    ALGORITHM="HS256"

CMD ["python3", "/devtrack/main.py"]