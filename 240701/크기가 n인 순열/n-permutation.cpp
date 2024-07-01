#include <iostream>
#include <vector>
#define MAX 9
using namespace std;

int n;
vector<int> v;
bool visited[MAX];

void permutate(int cnt) {
    if (cnt == n) {
        for (const auto& num : v) {
            cout << num << " ";
        }
        cout << "\n";
    }

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            v.push_back(i);
            visited[i] = true;
            permutate(cnt + 1);
            v.pop_back();
            visited[i] = false;
        }
    }
}


int main() {
    // 여기에 코드를 작성해주세요.
    ios::sync_with_stdio(false);
    cin.tie(0);

    cin >> n;
    permutate(0);

    return 0;
}