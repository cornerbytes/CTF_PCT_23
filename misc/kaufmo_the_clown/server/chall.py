#!/usr/bin/env python3
import os

if __name__ == "__main__":
    FLAG = os.getenv("FLAG")
    print("> ayo bantu kaufmo mencari pintu keluar")
    print("> bantu kaufmo untuk mencari kata sandi yang digunakan")
    user_input = input("masukkan kata sandi : ")
    user_input = user_input.replace("kaufmo", "")  # filter bad input

    if user_input == "kaufmo":
        print(f"ini flag mu : {FLAG} dan terima kasih telah membantu kaufmo!")
    elif user_input == "cheat":
        print("gak boleh cheat. https://www.youtube.com/watch?v=Y29XTh59F2g")
    else:
        print(f"kata sandi yang kamu masukkan : {user_input}")
        print("kata sandi salah")
