FROM ubuntu:18.04

RUN apt update \
&&  apt install -y python3 python3-pip \
&& apt clean

ADD requirements.txt /

RUN pip3 install -r /requirements.txt

ADD toowtrsywen /toowtrsywen/

RUN python3 /toowtrsywen/manage.py migrate

ENTRYPOINT ["python3", "/toowtrsywen/manage.py"]
CMD ["help"]

