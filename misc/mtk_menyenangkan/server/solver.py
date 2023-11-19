from pwn import *

if __name__ == "__main__":
    #p = process('./chall.py')
    p = remote('127.0.0.1', 1337)
    for i in range(25):
        data = p.recvuntil(b"?").decode().split('l : ')[1].replace(' ?', '')
        res = eval(data)
        p.recv()
        print(data, res)
        p.sendline(str(res).encode())

    print(p.recv().decode())
