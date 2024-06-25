#include <iostream>
#include <vector>

using namespace std;

int n, m;
vector<int> v;

void comb(int cnt, int k) {
    if (cnt == m) {
        for (const auto& num : v) {
            cout << num << " ";
        }
        cout << "\n";
    }
    for (int i = k; i <= n; i++) {
        v.push_back(i);
        comb(cnt + 1, i + 1);
        v.pop_back();
    }
}

int main() {
    // 여기에 코드를 작성해주세요.
    cin >> n >> m;
    comb(0, 1);

    return 0;
}