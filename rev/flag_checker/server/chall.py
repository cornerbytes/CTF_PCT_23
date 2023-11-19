def flag_checker(user_input):
    if len(user_input)==28: 
        if user_input[4] != 51:
            return False
        if user_input[4] - user_input[3] !=1:
            return False
        if user_input[15]*2 != 214:
            return False
        if user_input[1] + user_input [0] != 147:
            return False
        if user_input[11] != 99:
            return False
        if user_input[7] - user_input[11] != 9:
            return False
        if user_input[21] - user_input[18] != 21:
            return False
        if user_input[15]*2 - user_input[13] != 113:
            return False
        if user_input[14] * user_input[25] != 5049:
            return False
        if user_input[5] != 123:
            return False
        if user_input[0] + user_input[1] + user_input[2] !=231:
            return False
        if user_input[15] + user_input[11] + user_input[14] != 305:
            return False
        if user_input[21] + user_input[11] != 215:
            return False
        if user_input[0] * user_input[25] != 4080:
            return False
        if user_input[9]*2 != 206:
            return False
        if user_input[17] - user_input[9] != 11:
            return False
        if user_input[27] - user_input[25] !=74:
            return False
        if user_input[26] + user_input[27] + user_input[25] != 271:
            return False
        if user_input[26] != user_input[23]:
            return False
        if user_input[23] != user_input[10]:
            return False
        if user_input[6] *2 != 204:
            return False
        if user_input[12] - user_input[6] !=2:
            return False
        if user_input[12] - user_input[16] != 3:
            return False
        if user_input[22] /2 !=52:
            return False
        if user_input[20] - user_input[22] !=1:
            return False
        if user_input[24]*2 != 244:
            return False
        if user_input[24] + user_input[19] != 241:
            return False
        if user_input[8] !=97:
            return False

        print("CORRECT!.")
        print(f"here your flag : {userinput}")
        return True


if __name__ == "__main__":
    userinput = input("enter your flag: ")
    user_input = [ord(i) for i in userinput]
    if flag_checker(user_input) == False:
        print("Wrong Flag")
    else:
        pass
