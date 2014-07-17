FROM python:2.7
RUN curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python
RUN pip install docker-py==0.3.2
COPY docker-export-volumes.py /usr/local/bin/
ENTRYPOINT ["/usr/local/bin/docker-export-volumes.py"]
