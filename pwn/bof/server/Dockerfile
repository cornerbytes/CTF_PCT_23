FROM alpine:latest
EXPOSE 5000
WORKDIR /
RUN echo "x86" > /etc/apk/arch
RUN apk add --no-cache socat 'libc6-compat=1.2.4-r2'
COPY . .
CMD ["socat", "tcp-l:5000,reuseaddr,fork", "EXEC:'timeout 30s ./bof',stderr"]
