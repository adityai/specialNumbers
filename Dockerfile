FROM python:2.7
MAINTAINER adityaii@gmail.com
RUN apt-get update && apt-get install -y iputils-ping
WORKDIR /opt/
COPY ./*.py /opt/
COPY requirements.txt /opt/
RUN pip install -r requirements.txt
CMD python primeNumbers.py
