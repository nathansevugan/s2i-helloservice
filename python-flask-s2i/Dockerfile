#FROM ubuntu:latest
FROM python:2.7

LABEL MAINTAINER ranganathan.sevuganchetty@sabre.com
LABEL io.k8s.description="Platform for running python applications" \
      io.k8s.display-name="python-flask" \
      io.openshift.expose-services="5000:http" \
      io.openshift.tags="builder,html,flask"

ENV http_proxy http://sg0501095:4Garuda*1973@www-ad-proxy.sabre.com:80
ENV https_proxy http://sg0501095:4Garuda*1973@www-ad-proxy.sabre.com:80

USER root
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#RUN mkdir /app
WORKDIR /app

# install flask
RUN python --version
#RUN pip install Flask

# Although this is defined in openshift/base-centos7 image it's repeated here
# to make it clear why the following COPY operation is happening
LABEL io.openshift.s2i.scripts-url=image:///usr/local/s2i

# Copy the S2I scripts from ./.s2i/bin/ to /usr/local/s2i when making the builder image
COPY ./.s2i/bin/ /usr/local/s2i


# COPY ./helloservice.py /app
COPY ./requirements.txt /app

RUN chown -R 1001:1001 /app

RUN pip install -r ./requirements.txt


# run as non-root user
USER 1001

#ENTRYPOINT ["python"]
#CMD ["helloservice.py"]

#CMD [ "python", "./helloservice.py" ]
#CMD  [ "sh", "-c", "python /usr/src/app/helloservice.py&"]


# Default http port
EXPOSE 5000
