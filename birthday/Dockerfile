FROM alpine

ADD . /code

WORKDIR /code

RUN apk add py3-pip python3

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]

