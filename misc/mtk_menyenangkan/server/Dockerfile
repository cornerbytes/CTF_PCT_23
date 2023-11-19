FROM python:3.10-slim

RUN useradd -U -m -s /bin/bash ctf

RUN apt-get update
RUN apt install -y socat

WORKDIR /home/ctf
COPY chall.py ./ 

RUN chmod 500 /home/ctf/chall.py
RUN chown -R ctf:root /home/ctf

RUN pip install --upgrade pip
RUN pip install pycryptodome

ENV FLAG=PCT23{dont_tell_me_you_answer_this_question_manually_cbd9a2}

USER ctf

CMD socat TCP-L:7777,fork EXEC:"timeout 60s python3 /home/ctf/chall.py",reuseaddr,stderr
