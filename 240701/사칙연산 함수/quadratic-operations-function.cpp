#include <iostream>

int main() {
    int a;
    int b;
    char s;
    scanf("%d %c %d",&a,&s,&b);
    if(s=='+') {
        printf("%d + %d = %d",a,b,a+b);
    }
    else if (s=='-') {
        printf("%d - %d = %d",a,b,a-b);
    }
    else if (s=='/') {
        printf("%d / %d = %d",a,b,a/b);
    }
    else if (s=='*'){
        printf("%d * %d = %d",a,b,a*b);
    }
    else {
        printf("False");
    }
    return 0;
}