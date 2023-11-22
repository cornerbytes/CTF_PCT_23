#include <stdio.h>

void s3creT_b4s3()
{
    system("/bin/cat flag");
}

void welcome()
{
    char buffer[32];

    printf("Nama:\n");
    scanf("%s", buffer);
    printf("Selamat datang, %s\n", buffer);
}

int main()
{
    welcome();

    return 0;
}
