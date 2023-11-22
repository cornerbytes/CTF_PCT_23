FROM alpine:latest
EXPOSE 5000
WORKDIR /
RUN apk add --no-cache socat libc6-compat
COPY . .
CMD ["socat", "tcp-l:5000,reuseaddr,fork", "EXEC:'./welcomer2',stderr"]
