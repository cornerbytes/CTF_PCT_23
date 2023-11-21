FROM python:3.10-alpine

RUN adduser -D -u 1000 ctf

RUN apk --no-cache add socat

WORKDIR /home/ctf
COPY chall.py ./

RUN chmod 500 /home/ctf/chall.py
RUN chown -R ctf:root /home/ctf

RUN pip install --upgrade pip
RUN pip install pycryptodome

ENV FLAG=PCT23{sangat_gg_gggaming_breaking_cbc_mode_0cd6a8}

USER ctf

CMD socat TCP-L:1337,fork EXEC:"timeout 60s python3 /home/ctf/chall.py",reuseaddr,stderr
