############################################################
# Dockerfile to build Flask App
# Based on:
# https://github.com/Craicerjack/apache-flask/blob/master/Dockerfile
############################################################

# Set the base image
FROM ubuntu:xenial

# File Author / Maintainer
MAINTAINER timolin@gmail.com

RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    libxml2-dev \
    build-essential \
    python \
    python-dev\
    python-pip \
    vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

 # Copy over and install the requirements
 COPY ./app/requirements.txt /var/www/apache-flask/app/requirements.txt
 RUN pip install -r /var/www/apache-flask/app/requirements.txt

 # Copy over the apache configuration file and enable the site
 COPY ./apache-flask.conf /etc/apache2/sites-available/apache-flask.conf
 RUN a2ensite apache-flask
 RUN a2enmod headers

 # Copy over the wsgi file
 COPY ./apache-flask.wsgi /var/www/apache-flask/apache-flask.wsgi

 COPY ./run.py /var/www/apache-flask/run.py
 COPY ./app /var/www/apache-flask/app/

 RUN a2enmod proxy
 RUN a2enmod proxy_http
 RUN a2enmod proxy_html
 RUN a2enmod proxy_wstunnel
 RUN a2enmod rewrite

 RUN a2dissite 000-default.conf
 RUN a2ensite apache-flask.conf

 EXPOSE 80

 WORKDIR /var/www/apache-flask

 # CMD ["/bin/bash"]
 CMD  /usr/sbin/apache2ctl -D FOREGROUND
 # The commands below get apache running but there are issues accessing it online
 # The port is only available if you go to another port first
 # ENTRYPOINT ["/sbin/init"]
 # CMD ["/usr/sbin/apache2ctl"]
