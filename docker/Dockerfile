FROM ubuntu:20.04
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install sqlite3 -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y

ENV  requirements /home/requirements.txt

COPY requirements.txt ${requirements}

RUN pip3 install -r requirements

WORKDIR /home/
