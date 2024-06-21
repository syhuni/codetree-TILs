#include <iostream>
#include <vector>

using namespace std;

int k, n;
vector<int> ans_arr;


void Pick(int cnt) {
    if (cnt == n) {
        for (const auto& num : ans_arr) {
            cout << num << " ";
        }
        cout << "\n";
        return;
    }

    for (int i = 1; i <= k; i++) {
        ans_arr.push_back(i);
        Pick(cnt + 1);
        ans_arr.pop_back();
    }
}


int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> k >> n;
    Pick(0);
    return 0;
}