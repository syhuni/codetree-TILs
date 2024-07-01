#include <iostream>
#include <vector>
#include <algorithm>
#define MAX 10
using namespace std;

int n;
int matrix[MAX][MAX] = {0,};
bool visited[MAX];
vector<int> perm;
int max_val = 0;

void dfs(int cnt) {
    if (cnt == n) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += matrix[i][perm[i]];
        }
        max_val = max(max_val, sum);
        return;
    }

    for (int i = 0; i < n; i++) {
        if (visited[i]) {
            continue;
        }

        perm.push_back(i);
        visited[i] = true;

        dfs(cnt + 1);

        perm.pop_back();
        visited[i] = false;
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    
    dfs(0);
    cout << max_val;
    return 0;
}