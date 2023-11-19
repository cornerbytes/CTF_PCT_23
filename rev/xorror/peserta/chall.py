def xorror_checker(user_input):
    FLAG = [425, 1402, 429, 1291, 458, 1346, 400, 1361, 422, 1357, 408, 1362, 406, 1366, 406, 1357, 422, 1367, 384, 1368, 388]

    if len(user_input) != len(FLAG):
        return False

    for i, char in enumerate(user_input):
        xor_value = 505 if i % 2 == 0 else 1337
        if ord(char) ^ xor_value != FLAG[i]:
            return False

    return True

if __name__ == "__main__":
    print('> Selamat datang di program xorror yang sangat tidak menakutkan')
    print('> jika kamu dapat melakukan reverse program ini maka kamu akan mendapatkan flag')

    user_input = input('Masukkan Flag : ')
    
    if xorror_checker(user_input):
        print(f"Here's your flag: {user_input}")
    else:
        print("Wrong Flag")
