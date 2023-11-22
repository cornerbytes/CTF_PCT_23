FROM python:3.9-alpine3.15
WORKDIR /app
COPY . /app
RUN apk --no-cache add build-base libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base libffi-dev openssl-dev
RUN adduser --disabled-password --gecos '' nonrootuser
RUN apk --no-cache add curl
USER nonrootuser
EXPOSE 5000
ENV FLAG=PCT23{cyber_security_researcher_abal_abal}
CMD ["python", "app.py"]
