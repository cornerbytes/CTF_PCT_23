#include <stdio.h>

int main(){
	unsigned int random;
	random = rand();
	unsigned int key=0;
	printf("Berikan kunci nya!\n");
	scanf("%d", &key);

	if( (key ^ random) == 0xdeadbeef ){
		printf("Mantap, ini buat kamu!\n");
		system("/bin/cat flag");
		return 0;
	}

	printf("Uhh, cuman XOR doang kayaknya gampang deh '-'\n");
	return 0;
}

