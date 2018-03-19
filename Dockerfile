FROM python:2.7
ENV PYTHONUNBUFFERED 1
ENV DOCKER_RUN  TwylaBackend
RUN mkdir -p /config/reader/local/
ADD reader/requirements.pip /config/
ADD config/local/reader.ini /config/reader/local/
RUN pip install -r /config/requirements.pip
RUN mkdir /src
ADD reader/ /src/
WORKDIR /src



