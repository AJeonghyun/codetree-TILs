#include <iostream>
using namespace std;
int Abc(int a, int b) {
        int sum=0;
        for(int i=a; i<=b; i++) {
            if(i%2==0) continue;
            else if(i%10==5) continue;
            else if(i%3==0 && i%9!=0) continue;
            sum++;
        }
        return sum;
}
int main() {
    int a;
    int b;
    cin >> a >> b;
    cout << Abc(a,b);
}