import subprocess

if __name__ == "__main__":
    for i in range(1000, 0, -1):
        filename_pass = f"pass_{i}.txt"
        filename_zip = f"{i}.zip"
        with open(filename_pass, 'r') as f: password = f.read()

        subprocess.run(["unzip", "-P", password, filename_zip])
        subprocess.run(["rm", filename_zip, filename_pass])
    with open('flag.txt', 'r') as f: print(f.read())

