FROM centos:latest
MAINTAINER Sinchan

RUN yum -y install httpd mod_ssl

COPY server.crt /etc/pki/tls/certs/localhost.crt
COPY server.key /etc/pki/tls/private/localhost.key

EXPOSE 443

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

