import gzip
import bz2

if __name__ == "__main__":

    with open('flag.txt', 'w') as f: f.write("PCT23{zap_zip_zup_zep_zop_zipppp}")
    with open('flag.txt', 'r') as f: flag = f.read().encode()

    data = gzip.compress(flag)
    data = bz2.compress(data)
    with open('flag', 'wb') as f: f.write(data)
