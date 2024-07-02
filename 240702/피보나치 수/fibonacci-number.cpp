#include <iostream>
#define MAX 46

using namespace std;

int n;
int memo[MAX] = {-1,};

int fibbo(int n) {
    if (memo[n]) {
        return memo[n];
    }

    if (n <= 2) {
        memo[n] = 1;
        return memo[n];
    }

    memo[n] = fibbo(n - 1) + fibbo(n - 2);
    return memo[n]; 
}




int main() {
    cin >> n;
    cout << fibbo(n);
    return 0;
}