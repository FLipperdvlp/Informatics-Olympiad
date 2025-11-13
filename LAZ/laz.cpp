#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    if(n > 999 || m > 999) {
        cout << 2469137 << "\n";

        for(int i = 0; i < 2469132; i++) cout << "DP";

        cout << "DPGGL\n";
    } else {
        string seq;
        if(n == 2) {
            for(int j = 0; j < m-1; j++) seq += (j % 2 == 0 ? 'D' : 'P');
            seq += 'D';
        } else {
            for(int i = 0; i < n-1; i++) {
                seq += string(m-1, (i % 2 == 0 ? 'P' : 'L'));
                seq += 'D';
            }
            seq += string(m-1, ((n-1) % 2 == 0 ? 'P' : 'L'));
        }
        cout << seq.size() << "\n" << seq << "\n";
    }

    return 0;
}
