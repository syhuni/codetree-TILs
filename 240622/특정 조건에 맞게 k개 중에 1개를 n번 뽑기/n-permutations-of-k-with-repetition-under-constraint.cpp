#include <iostream>
#include <vector>

using namespace std;

int k, n;
vector<int> v;

void dfs() {
    if (v.size() == n) {
        for (const auto& num : v) {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }
    for (int i = 1; i <= k; i++) {
        if (v.size() >= 2) {
            if (i == v[v.size() - 2] && i == v[v.size() - 1]) {
                continue;
            }
        }
        v.push_back(i);
        dfs();
        v.pop_back();
    }
}


int main() {
    ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    cin >> k >> n;
    dfs();

    return 0;
}