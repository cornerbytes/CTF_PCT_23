#include <stdio.h>

void flag(int key){
	char flag[32];
	printf("berikan kunci untuk memastikan identitas : \n");
	scanf("%s", &flag);
	if(key != 0xdeadbeef){
		printf("\nhoho, ez banget yak!\n");
		system("/bin/cat flag");
	}
	else{
		printf("kayaknya kamu kurang semangat deh!\n");
	}
}
int main(int argc, char* argv[]){
	flag(0xdeadbeef);
	return 0;
}

