FROM ubuntu:eoan

RUN apt-get update
RUN apt-get install -y wget bzip2
RUN apt-get install -y build-essential
RUN apt-get install python3 python3-pip -y

RUN pip3 install flask pandas numpy


RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY classifier.py .
COPY server.py .
COPY stopWordsFR.txt .

EXPOSE 5000

CMD python3 server.py