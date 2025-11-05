#include <bits/stdc++.h>
using namespace std;

int n, q;
vector<string> grid;
vector<vector<int>> dist;

int dx[] = {-1,1,0,0};
int dy[] = {0,0,-1,1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    grid.resize(n);
    for (int i = 0; i < n; i++) cin >> grid[i];

    dist.assign(n, vector<int>(n, -1));
    queue<pair<int,int>> bfs;
    dist[0][0] = 0;
    bfs.push({0,0});

    while (!bfs.empty()) {
        auto [x, y] = bfs.front(); bfs.pop();
        for (int d=0; d<4; d++) {
            int nx = x + dx[d], ny = y + dy[d];
            if (nx>=0 && nx<n && ny>=0 && ny<n && grid[nx][ny]!='#' && dist[nx][ny]==-1) {
                dist[nx][ny] = dist[x][y] + 1;
                bfs.push({nx, ny});
            }
        }
    }

    set<pair<int,int>> forts;
    for (int i=0; i<n; i++)
        for (int j=0; j<n; j++)
            if (grid[i][j]=='F') forts.insert({i,j});

    auto get_max_dist = [&]() {
        int mx = 0;
        for (auto [x,y]: forts) mx = max(mx, dist[x][y]);
        return mx;
    };

    cout << get_max_dist() << "\n";

    for (int i=0; i<q; i++) {
        int x, y; cin >> x >> y; x--; y--;
        if (forts.count({x,y})) forts.erase({x,y});
        else forts.insert({x,y});
        cout << get_max_dist() << "\n";
    }

    return 0;
}
