FROM python:3.10-slim

RUN useradd -U -m -s /bin/bash ctf

RUN apt-get update
RUN apt install -y socat

WORKDIR /home/ctf
COPY chall.py ./ 

RUN chmod 500 /home/ctf/chall.py
RUN chown -R ctf:root /home/ctf

ENV FLAG=PCT23{the_amazing_digital_circus}

USER ctf

CMD socat TCP-L:2023,fork EXEC:"timeout 60s python3 /home/ctf/chall.py",reuseaddr,stderr
