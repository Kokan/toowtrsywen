FROM ubuntu:18.04

RUN apt update \
&&  apt install -y python3 python3-pip \
&& apt clean

ADD requirements.txt /

RUN pip3 install -r /requirements.txt

ADD toowtrsywen /toowtrsywen/

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN /toowtrsywen/reset-database

ENTRYPOINT ["python3", "/toowtrsywen/manage.py"]
CMD ["help"]

