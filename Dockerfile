
FROM ubuntu:20.04


RUN apt-get update && apt-get install -y python3 python3-pip


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


RUN pip3 install -r requirements.txt

COPY . /code

EXPOSE 8080


CMD ["python3", "nodo.py"]
