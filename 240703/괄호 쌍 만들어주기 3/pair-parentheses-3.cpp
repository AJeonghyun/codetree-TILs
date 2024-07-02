#include <iostream>
#include <string>
using namespace std;
int main() {
    string str;
    getline(cin,str);
    int sum = 0;
    for (int i=0; i<str.length(); i++) {
        for (int j=i+1; j<str.length(); j++) {
            if (str[i]=='(') {
                if (str[j]==')') {
                    sum += 1;
                }
                else {
                }
            }
            else {
            } 
        }
    }
    cout << sum;

    return 0;
}