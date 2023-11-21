FROM alpine:latest
WORKDIR /app
COPY main /app/
RUN apk add --no-cache socat

ENV FLAG=PCT23{the_amazing_digital_circus}
CMD ["socat", "tcp-l:2023,reuseaddr,fork", "EXEC:'timeout 30s ./main',stderr"]
