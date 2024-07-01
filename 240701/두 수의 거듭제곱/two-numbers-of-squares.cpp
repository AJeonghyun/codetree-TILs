#include <iostream>

int main() {
    int a;
    int b;
    int sum = 1;
    scanf("%d %d",&a,&b);
    for(int i=0; i<b; i++) {
        sum *= a;
    }
    printf("%d",sum);
    return 0;
}