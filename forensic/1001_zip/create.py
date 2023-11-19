import subprocess
import secrets
if __name__ == "__main__":

    for i in range(1000):
        password = secrets.token_hex(3)
        filename_zip = f"{i+1}.zip"
        filename_pass = f"pass_{i+1}.txt"

        if i==0:
            with open(filename_pass, 'w') as f: f.write(password)
            subprocess.run(["zip", "-e", "-P", password, "1.zip", "flag.txt", filename_pass])
        else:
            filename_zip_before = f"{i}.zip"
            filename_pass_before = f"pass_{i}.txt"
            with open(filename_pass, 'w') as f: f.write(password)
            subprocess.run(["zip", "-e", "-P", password, filename_zip, filename_zip_before, filename_pass_before])
            subprocess.run(["rm", filename_pass_before, filename_zip_before])

