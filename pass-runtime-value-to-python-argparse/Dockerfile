FROM centos:7

USER root

RUN yum install -y python36-devel python36-pip

COPY . /app

RUN ls -l /app

ENTRYPOINT ["python","/app/app.py"]