from pwn import *

if __name__ == "__main__":

    # send payload 'a'*16
    #p = process('./chall.py')
    p = remote('127.0.0.1', 9999)

    payload = b'a'*16
    p.recv()
    p.sendline(b'1')
    p.recv()
    p.sendline(payload)

    # recv ciphertext of 'a'*16
    ciphertext = p.recvuntil(b'\n').decode().split(' = ')[1].strip()

    # get encrypted secret
    p.recv()
    p.sendline(b'2')
    encrypted_secret = p.recvuntil(b'\n').decode().split(' = ')[1].strip()

    # calculate the key
    ciphertext = bytes.fromhex(ciphertext)
    encrypted_secret = bytes.fromhex(encrypted_secret)
    first_block = xor(ciphertext, payload)
    key = xor(encrypted_secret, first_block)
    
    # submit flag 
    p.recv()
    p.sendline(b'3')
    p.recv()
    p.sendline(key.hex().encode())
    print(p.recvuntil(b'\n').decode())
