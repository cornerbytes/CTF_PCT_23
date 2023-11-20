#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os


def menu() -> str:
    print("> Welcome to my service")
    print(
        "> you need to figure out how cbc mode in AES work and submit the key then you get the flag"
    )
    print("[1] encrypt")
    print("[2] decrypt")
    print("[3] submit key")
    print("[4] exit")
    print("[5] cheat")

    return input("enter your choice : ")


def encrypt(KEY: bytes):
    cipher = AES.new(key=KEY, mode=AES.MODE_CBC, iv=KEY)
    plaintext = input("enter your plaintext : ").encode()
    if len(plaintext) % 16 != 0:
        plaintext = pad(plaintext, 16)
    result = cipher.encrypt(plaintext).hex()
    print(f"Here your ciphertext : {result}")


def decrypt(KEY: bytes):
    cipher = AES.new(key=KEY, mode=AES.MODE_CBC, iv=KEY)
    ciphertext = bytearray.fromhex(input("enter your ciphertext in hexadecimal : "))

    # padding the user input if size less than 16
    if len(ciphertext) % 16 != 0: ciphertext = pad(ciphertext, 16)

    # check the result type after decrypting the ciphertext
    try:
        result = cipher.decrypt(ciphertext)
        result = result.decode().strip()
    except ValueError: pass

    if isinstance(result, bytes): 
        print(f"bytes detected, Here your plaintext in hexadecimal : {result.hex()}")
    else:
        print(f"here your plaintext : {result}")

def submit_key():
    user_input_key = input("Enter the key : ")
    user_input_key = bytes.fromhex(user_input_key)
    if user_input_key == KEY:
        print(f"here your flag : {FLAG}")
    else:
        print(f"wrong key! try again")


if __name__ == "__main__":
    KEY = os.urandom(16)
    FLAG = os.getenv("FLAG")

    while True:
        user_choice = menu()
        if user_choice == "1":
            encrypt(KEY)
        elif user_choice == "2":
            decrypt(KEY)
        elif user_choice == "3":
            submit_key()
        elif user_choice == "4":
            break
        elif user_choice == "5":
            print(
                "there is no shortcut. Here, take the blackpill : https://www.youtube.com/watch?v=3mVqH6-D-HA"
            )
