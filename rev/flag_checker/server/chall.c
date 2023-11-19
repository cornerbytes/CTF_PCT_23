#include <stdio.h>
int flag_checker(char user_input[], int size) {
  if (size == 28) {
        if (user_input[4] != 51) {
            return 0;
        }
        if (user_input[4] - user_input[3] != 1) {
            return 0;
        }
        if (user_input[15] * 2 != 214) {
            return 0;
        }
        if (user_input[1] + user_input[0] != 147) {
            return 0;
        }
        if (user_input[11] != 99) {
            return 0;
        }
        if (user_input[7] - user_input[11] != 9) {
            return 0;
        }
        if (user_input[21] - user_input[18] != 21) {
            return 0;
        }
        if (user_input[15] * 2 - user_input[13] != 113) {
            return 0;
        }
        if (user_input[14] * user_input[25] != 5049) {
            return 0;
        }
        if (user_input[5] != 123) {
            return 0;
        }
        if (user_input[0] + user_input[1] + user_input[2] != 231) {
            return 0;
        }
        if (user_input[15] + user_input[11] + user_input[14] != 305) {
            return 0;
        }
        if (user_input[21] + user_input[11] != 215) {
            return 0;
        }
        if (user_input[0] * user_input[25] != 4080) {
            return 0;
        }
        if (user_input[9] * 2 != 206) {
            return 0;
        }
        if (user_input[17] - user_input[9] != 11) {
            return 0;
        }
        if (user_input[27] - user_input[25] != 74) {
            return 0;
        }
        if (user_input[26] + user_input[27] + user_input[25] != 271) {
            return 0;
        }
        if (user_input[26] != user_input[23]) {
            return 0;
        }
        if (user_input[23] != user_input[10]) {
            return 0;
        }
        if (user_input[6] * 2 != 204) {
            return 0;
        }
        if (user_input[12] - user_input[6] != 2) {
            return 0;
        }
        if (user_input[12] - user_input[16] != 3) {
            return 0;
        }
        if (user_input[22] / 2 != 52) {
            return 0;
        }
        if (user_input[20] - user_input[22] != 1) {
            return 0;
        }
        if (user_input[24] * 2 != 244) {
            return 0;
        }
        if (user_input[24] + user_input[19] != 241) {
            return 0;
        }
        if (user_input[8] != 97) {
            return 0;
        }

        printf("CORRECT!.\n");
        printf("here your flag : %s\n", user_input);
        return 1;
    }

    return 0;
}

int main() {
    char user_input[28];
    printf("enter your flag: ");
    scanf("%s", user_input);

    if (flag_checker(user_input, sizeof(user_input) / sizeof(user_input[0])) == 0) {
        printf("Wrong Flag\n");
    }

    return 0;
}
