from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes


def read_flag() -> str:
    try:
        with open('flag.txt', 'r') as f:
            return f.read()
    except:
        print('file flag.txt not found')

def encrypt(n, e, FLAG):
    for i in range(len(FLAG)):
        m = bytes_to_long(FLAG[i].encode())
        ciphertext = pow(m, e, n)
        with open(f"ransom/{i}.enc", 'wb') as f:
            ciphertext = long_to_bytes(ciphertext)
            f.write(ciphertext)


if __name__ == "__main__":
    key = RSA.generate(2048)
    n = key.n 
    e = key.e 
    FLAG = read_flag()
    encrypt(n, e, FLAG)

    # export the public key
    publickey = key.publickey().export_key()
    with open("public_key.pem", "wb") as f:
        f.write(publickey)



