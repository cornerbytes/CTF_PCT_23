#include <stdio.h>

void flag(int key){
	char flag[64];
	printf("Apa yang sedang kamu pikirkan? : \n");
	scanf("%s", &flag);
	if(key == 0xcafebabe){
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

