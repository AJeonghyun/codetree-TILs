#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int arr[100];
    int sum = 0;
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    for (int i=0; i<n; i++) {
        for (int j=i+1; j<n-1; j++) {
            for (int k=i+2; k<n; k++) {
                if ((i<j) && (j<k)) {
                    if((arr[i] < arr[j])&& (arr[j] < arr[k])) {
                        sum += 1;
                    }  
                }
            }
        }
    }
    cout << sum;

    return 0;
}