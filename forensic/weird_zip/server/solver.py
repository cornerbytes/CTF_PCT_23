import gzip
import bz2

if __name__ == "__main__":

    with open('flag', 'rb') as f: data = f.read()
    data = bz2.decompress(data)
    data = gzip.decompress(data)
    print(data)
