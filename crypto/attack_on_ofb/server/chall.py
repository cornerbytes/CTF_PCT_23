#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import bytes_to_long, long_to_bytes
import os

def encrypt(data):
    if len(data)%16 !=0: data = pad(data, 16)
    cipher = AES.new(KEY, AES.MODE_OFB, IV)
    data = cipher.encrypt(data)
    return data.hex()

def menu():
    print("> welcome to my service")
    print("> if you can guess the secret and break ofb mode you can get your flag")
    print("1. Encrypt")
    print("2. Get Encrypted Secret")
    print("3. Get flag")
    print("4. exit")
    return input("Enter your Choice : ")

if __name__ == "__main__":
    KEY = os.urandom(16)
    IV  = os.urandom(16)
    FLAG = os.getenv('FLAG')
    secret = os.urandom(16)

    while True:
        try:
            user_choice = menu()
            if user_choice == '1':
                data = input("Plaintext : ").encode()
                print(f"ciphertext = {encrypt(data)}")
            elif user_choice == '2':
                print(f"ciphertext of secret = {encrypt(secret)}")
            elif user_choice == '3':
                user_guess = input('enter secret in hexadecimal : ') 
                user_guess = bytes.fromhex(user_guess)
                if user_guess == secret:
                    print(f"here your flag : {FLAG}")
                else: print("Wrong secret")
            elif user_choice == '4': break
        except:
            print('Error')
            break
