#include <iostream>
#include <cstdlib>
#include <climits>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int arr[1000];
    for(int k=0; k<n; k++) {
        cin >> arr[k];
    }

    int min_num = INT_MAX;
    for (int i=0; i<n; i++) {
    int sum = 0;
        for (int j=0; j<n; j++) {
            sum += abs(arr[j]*(j-i));
        }
        min_num = min(sum,min_num);
    }
    cout << min_num;
    return 0;
}