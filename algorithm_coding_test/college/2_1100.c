#include <stdio.h>

int main() {
    int count = 0;

    for (int i = 0; i < 8; i++) {
        char chessLine[9];  // 8글자 + 널문자 ('\0') 고려하여 크기 9로 설정
        scanf("%s", chessLine);

        for (int j = 0; j < 8; j++) {
            if ((i + j) % 2 == 0 && chessLine[j] == 'F') {  
                count++; 
            }
        }
    }

    printf("%d\n", count);
    return 0;
}
