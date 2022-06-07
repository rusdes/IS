#include <stdio.h>

int main(){
    char a[4];
    fgets(a, 4, stdin);
    printf("%s", a);
    return 0;
}