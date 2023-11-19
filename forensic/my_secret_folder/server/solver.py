import subprocess
if __name__ == "__main__":
    res = subprocess.run(['git', 'log', '-n', '50','--pretty=format:"%h"'], capture_output=True, text=True)
    log_history = res.stdout.replace("\"", "").split("\n")
    log_history.reverse()
    flag = ""
    for i in log_history:
        subprocess.run(['git', 'checkout', i])
        char = subprocess.run(['cat', 'flag.txt'], capture_output=True, text=True)
        flag += char.stdout.strip()
    print(flag)
