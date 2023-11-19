from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes


def read_enc_flag() -> list:
    res = []
    for i in range(42):
        filename = f"ransom/{i}.enc"
        with open(filename, 'rb') as f:
            ciphertext = f.read()
            ciphertext = bytes_to_long(ciphertext)
            res.append(ciphertext)
    return res

def read_public_key(filename) -> tuple:
    with open(filename, 'r') as f:
        public_key = RSA.import_key(f.read())
    return public_key.e, public_key.n 


def rainbow_table(e, n):
    res = dict()
    list_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_"
    for i in list_char:
        m = bytes_to_long(i.encode())
        ciphertext = pow(m, e, n)
        res[ciphertext] = i
    return res


if __name__ == "__main__":
    e, n = read_public_key('public_key.pem')
    flag_enc = read_enc_flag()
    rainbow_table = rainbow_table(e, n)
    flag_enc.pop(41)

    for i in flag_enc:
        print(rainbow_table[i],end="")
