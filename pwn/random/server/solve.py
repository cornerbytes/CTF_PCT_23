#!/usr/bin/env python3

from pwn import *

io = process('./random')
#io = remote('172.17.0.2',5000)

payload = b'3039230856'

io.recv()
io.sendline(payload)
io.interactive()
