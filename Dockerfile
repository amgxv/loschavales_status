from alpine

COPY app /app/
WORKDIR /app

ENV SERVER=changeme
RUN apk update && \
apk add python3
RUN pip3 install -r requirements.txt

ENTRYPOINT gunicorn -w 2 -b 0.0.0.0:5000 status:app