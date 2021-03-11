#include <stdio.h>

int square (int i){
    return i*i;
}

int add (int x, int y){
    return x + y;
}

int subtract (int x, int y){
    return x - y;
}

void printer(int d){
    int x = 98;
    for (int i=0; i<d; i++){
        i = i + x;
        i = i - x;
        printf("%d\n",i);
    }
}

int main(){
    printer(100000);
    return 0;
}