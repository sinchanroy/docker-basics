FROM ubuntu:latest

RUN mkdir -p /etc/apache2/ssl/

COPY index.html /var/www/html/app/htdocsAdmin/


ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

RUN apt-get update \
  && apt-get install -y apache2  apache2-utils openssl 

RUN openssl req -new -newkey rsa:4096 -days 3650 -nodes -x509 -subj     "/C=DE/ST=BAV/L=MUN/O=VKB/CN=reply"     -keyout ./ssl.key -out ./ssl.crt
RUN cp ./ssl.crt /etc/apache2/ssl/ssl.crt
RUN cp ./ssl.key /etc/apache2/ssl/ssl.key

ADD 000-default.conf /etc/apache2/sites-available/000-default.conf

RUN a2enmod rewrite
RUN a2enmod ssl

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

