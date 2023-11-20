from hashlib import sha256
from os import urandom
if __name__ == "__main__":
    
    while True:
        nonce = urandom(16).hex()
        nonce = nonce
        hash_result = sha256(nonce.encode()).hexdigest()
        if hash_result.startswith("0000"): 
            print(nonce, hash_result)
            break
