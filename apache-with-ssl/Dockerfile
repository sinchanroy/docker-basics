FROM centos:latest
MAINTAINER Sinchan

RUN yum -y install httpd mod_ssl

RUN mkdir -p /etc/ssl/private
RUN chmod 700  /etc/ssl/private

COPY public-html/index.html /var/www/html/

COPY ./server.crt /etc/apache2/ssl/server.crt
COPY ./server.key /etc/apache2/ssl/server.key
RUN mkdir -p /var/run/apache2/

COPY ./ssl.conf /etc/httpd/conf.d/
COPY httpd.conf /etc/httpd/conf/httpd.conf

EXPOSE 80

CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

