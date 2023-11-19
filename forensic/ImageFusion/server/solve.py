#!/usr/bin/env python3

with open('stacked.png', 'rb') as stack:
    flag = stack.read()
stack.close()

flag1 = flag[:len(flag)//2].strip(bytes(0))
flag2 = flag[len(flag)//2:].strip(bytes(0))

with open('flag1.png', 'wb') as flag:
    flag.write(flag1)
flag.close
with open('flag2.png', 'wb') as flag:
    flag.write(flag2)
flag.close
