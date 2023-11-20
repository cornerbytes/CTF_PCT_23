from hashlib import sha256
from os import urandom, getenv
if __name__ == "__main__":
    FLAG = getenv("FLAG")
    print("> welcome to bitcoin mining")
    print("> this program using sha256 algorithm to calculate the hash")
    print("> you must find the right value to get the result of sha256 that startswith 4 trailing zeros")
    while True:
        nonce = input('enter a value : ')
        nonce = nonce.encode()
        hash_result = sha256(nonce).hexdigest()
        if hash_result.startswith("0000"): 
            print(f"here your flag : {FLAG}")
            break
