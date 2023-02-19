# include <stdio.h>

void dec2bin(long* res, long num);

int main() {
    long num = 7837589734983249234629746238749289;
    long result[1024];
    dec2bin(result, num);
    int count = 0;
    while (result[count] != -1) {
        printf("%d", result[count]);
        count++;
    }
    return 0;
}

// 将十进制转为二进制
void dec2bin(long* res, long num) {
    int count = 0;
    while(num > 0) {
        res[count] = num % 2;
        num = num / 2;
        count++;
    }
    res[count] = -1;
}
