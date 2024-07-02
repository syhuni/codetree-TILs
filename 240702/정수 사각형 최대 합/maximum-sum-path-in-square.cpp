#include <iostream>
#include <algorithm>
#define MAX 100

using namespace std;

int n;
int matrix[MAX][MAX] = {0,};
int dp[MAX][MAX] = {0,};


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    
    // dp 초기 조건
    for (int i = 1; i < n; i++) {
        matrix[0][i] += matrix[0][i - 1];
        matrix[i][0] += matrix[i - 1][0];
    }
    
    for (int i = 1; i < n; i++) {
        for (int j = 1; j < n; j++) {
            matrix[i][j] += max(matrix[i - 1][j], matrix[i][j - 1]);
        }
    }

    int ans = *max_element(matrix[n - 1], matrix[n - 1] + n);
    cout << ans;

    return 0;
}