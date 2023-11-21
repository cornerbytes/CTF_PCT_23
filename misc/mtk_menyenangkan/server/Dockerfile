FROM alpine:latest
WORKDIR /app
COPY main /app/
RUN apk add --no-cache socat

ENV FLAG=PCT23{dont_tell_me_you_answer_this_question_manually_cbd9a2}
CMD ["socat", "tcp-l:7777,reuseaddr,fork", "EXEC:'./main',stderr"]
