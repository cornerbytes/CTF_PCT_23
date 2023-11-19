#!/usr/bin/env python3

import os 
import random


def init_menu():
    print("> SELAMAT DATANG DI UJIAN MTK PART 1")
    print("> KALIAN AKAN MENDAPATKAN FLAG JIKA BERHASIL MENCAPAI SKOR 25")
    

def question():
    operator = random.choice(["kali", "tambah", "kurang"])
    x = random.randint(1, 50)
    y = random.randint(1, 50)
    if operator == "kali":
        answer = x*y
        print(f"Soal : {x} * {y} ?")
        user_input = int(input('Jawaban : '))
        if user_input == answer: return True 
        else : return False
    elif operator == "tambah":
        answer = x+y
        print(f"Soal : {x} + {y} ?")
        user_input = int(input('Jawaban : '))
        if user_input == answer: return True 
        else : return False
    
    if operator == "kurang":
        answer = x-y
        print(f"Soal : {x} - {y} ?")
        user_input = int(input('Jawaban : '))
        if user_input == answer: return True 
        else : return False

if __name__ == "__main__":
    FLAG = os.getenv('FLAG')
    SKOR = 0     
    init_menu()
    try:
        while (SKOR!=25):
            if question():
                SKOR +=1
                print(f'SKOR : {SKOR}\n')
            else:
                SKOR -=1
                print(f'SKOR : {SKOR}\n')
            if SKOR==25:
                print(f"CONGRATULATIONS. HERE YOUR FLAG {FLAG}")
                
    except ValueError:
        print('Input Error. Hanya Boleh angka')
