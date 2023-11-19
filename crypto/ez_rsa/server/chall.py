from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

if __name__ == "__main__":
    p = getPrime(512)
    q = getPrime(512)
    e = 65537
    n = p * q
    
    try:
        with open('flag.txt', 'r') as f:
            flag = f.read().encode()
            flag = bytes_to_long(flag)
    except:
        print("flag.txt not found")
        exit()

    c = pow(flag, e ,n)
    with open('flag_ez_rsa.txt', 'w') as f:
        f.write(f"c = {c}\n")
        f.write(f"e = {e}\n")
        f.write(f"p = {p}\n")
        f.write(f"q = {q}\n")
