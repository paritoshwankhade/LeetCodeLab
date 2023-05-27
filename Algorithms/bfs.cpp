#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<vector<int>> adjacencyList;

vector<vector<int>> bfs(vector<vector<int>>& adjacencyList, int numNodes, int source) {
    vector<bool> visited(numNodes, false);
    vector<int> distances(numNodes), parents(numNodes);
    queue<int> queue;

    queue.push(source);
    visited[source] = true;
    distances[source] = 0;
    parents[source] = -1;

    while (!queue.empty()) {
        int node = queue.front();
        queue.pop();
        cout << node << endl;

        for (auto neighbor : adjacencyList[node]) {
            if (!visited[neighbor]) {
                queue.push(neighbor);
                visited[neighbor] = true;
                distances[neighbor] = distances[node] + 1;
                parents[neighbor] = node;
            }
        }
    }

    return {distances, parents};
}

void printPath(const vector<int>& parents, int target) {
    vector<int> path;

    if (parents[target] == -1) {
        cout << "No path!";
    } else {
        while (target != -1) {
            path.push_back(target);
            target = parents[target];
        }
        reverse(path.begin(), path.end());
        cout << "Path: ";
        for (int node : path) {
            cout << node << " ";
        }
    }
    cout << endl;
}

int main() {
    int numNodes;
    int source;

    vector<int> distances;
    vector<int> parents;

    tie(distances, parents) = bfs(adjacencyList, numNodes, source);

    int target;
    printPath(parents, target);

    return 0;
}
