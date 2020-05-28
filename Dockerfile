FROM python:3.7.3-slim-stretch

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# The official Debian and Ubuntu images automatically run apt-get clean,
# so explicit invocation is not required.
RUN apt-get update && apt-get install -y \
    build-essential python3-dev \
	&& pip3 install -r requirements.txt\
	&& rm -rf /root/.cache/pip \
    && apt-get autoremove -y\
    && rm -rf /var/lib/apt/lists/*

COPY ./ /code
