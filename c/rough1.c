#include <stdio.h>

int func(int x, int y) {
    return x + y;
}

int main() {
    int a, b;
    a = 12;
    b = 7;
    printf("%d", func(a, b));
    return 0;
}