#include <iostream>
#define MAX 1001

using namespace std;

int n;
int stair[MAX] = {0,};

int main() {
    cin >> n;
    stair[2] = 1;
    stair[3] = 1;

    if (n < 4) {
        cout << stair[n];
    } 
    else {
        for (int i = 4; i <= n; i++) {
            stair[i] = (stair[i - 2] + stair[i - 3]) % 10007;
        }
        cout << stair[n];
    }
    return 0;
}