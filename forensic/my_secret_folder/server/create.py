import subprocess
import os
if __name__ == "__main__":
    
    #read flag
    with open('flag.txt', 'r') as f:
        flag = f.read()
    # init git
    subprocess.run(['mkdir', 'folder_rahasia'])
    subprocess.run(['touch', 'folder_rahasia/flag.txt'])
    subprocess.run(['git', 'init', 'folder_rahasia'])
 
    work_dir = os.getcwd()
    for i in flag:
        os.chdir(work_dir+"/folder_rahasia/")
        with open("flag.txt", "w") as flag_file:
            flag_file.write(i)
        subprocess.run(['git', 'add', 'flag.txt'])
        subprocess.run(['git', 'commit', "-m", "where is the flag?"])
