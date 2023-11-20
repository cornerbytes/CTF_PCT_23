from pwn import *
import codecs
if __name__ == "__main__":
   #p = process('./chall.py')
   p = remote("127.0.0.1", 1337)

   ## get the c1
   payload = (b'a'*16)
   p.recv()
   p.sendline(b'1')
   p.recv()
   p.sendline(payload)
   c1 = p.recvuntil(b'\n').decode().split(' : ')[1].strip()
   c1 = bytes.fromhex(c1)

   ## here the nullbytes trick
   p.recv()
   p.sendline(b'2')
   p.recv()
   payload = c1 + (b'\x00'*16) + c1
   p.sendline(payload.hex().encode())
   plaintext = p.recvuntil(b'\n')
   plaintext = plaintext.decode().split('plaintext in hexadecimal : ')[1].strip()
   plaintext = bytes.fromhex(plaintext)
   p1 = plaintext[:16]
   p3 = plaintext[32:]

   ## calculate key
   key = xor(p1, p3)
   key = key.hex().encode()

   # submit key 
   p.recv()
   p.sendline(b'3')
   p.recv()
   print(f"key: {key}")
   p.sendline(key)
   print(p.recvuntil(b'\n'))