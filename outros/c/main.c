#include <stdio.h>

int main() {
    int b;
    b = 10;
    int e = -3;
    int r = 1;

    for (int i=0; i<e; i++) {
        r *= b;
    }

    printf("%d\n", r);

    return 0;
};