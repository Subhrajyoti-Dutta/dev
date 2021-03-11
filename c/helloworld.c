#include <stdio.h>

int main(int argc, char *argv[]){
    FILE *p, *pp;
    int n;
    float f = 100.54;
    int a = 4, b = 34;
    char ch[12] = "BSCPMK";
    char str[50];
    if ((p=fopen("BSC.txt","wb+"))==NULL){
        printf("\n Failed");
    }
    for (int i=0; i<50; i++){
        printf("\n");
        printf("%d",i);
    }
    return 0;
}