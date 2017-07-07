FROM  python:2.7-alpine

COPY requirements.txt /tmp/requirements.txt
RUN  pip install -r /tmp/requirements.txt

CMD ["python", "/src/project/tests"]
