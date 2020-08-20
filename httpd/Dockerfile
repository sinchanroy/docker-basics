FROM httpd:latest



COPY ./server.crt  /usr/local/apache2/conf/
COPY ./server.key  /usr/local/apache2/conf/

#COPY index.html /usr/local/apache2/htdocs/

COPY my-httpd-ssl.conf /usr/local/apache2/conf/extra/httpd-ssl.conf

COPY my-httpd.conf /usr/local/apache2/conf/httpd.conf

EXPOSE 5000

CMD httpd -DFOREGROUND

