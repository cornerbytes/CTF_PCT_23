if __name__ == "__main__":
    FLAG = [425, 1402, 429, 1291, 458, 1346, 400, 1361, 422, 1357, 408, 1362, 406, 1366, 406, 1357, 422, 1367, 384, 1368, 388]
    RESULT = []
    for index, value in enumerate(FLAG):
        if index % 2 == 0: RESULT.append(value^505)
        else: RESULT.append(value^1337)
   
    for i in RESULT: print(chr(i), end="")
