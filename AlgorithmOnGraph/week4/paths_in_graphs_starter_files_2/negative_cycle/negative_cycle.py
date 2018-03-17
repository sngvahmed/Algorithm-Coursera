#Uses python3

import sys
vis = [0] * 1000
def bellmanFord(adj, cost, s):
    totalEdge = []
    node = []

    def relax(curArr, nd):
        if nd[0] > (node[curArr[0]][0] + curArr[2]):
            return True
        return False

    for i in range(0,adj.__len__()):
        if (i == s):
            node.append((0, None))
        else:
            node.append((sys.maxsize, None))

        for j in range(0,adj[i].__len__()):
            totalEdge.append((i , adj[i][j], cost[i][j]))

    itr = 0
    while (itr < adj.__len__() - 1):
        itr = itr + 1
        for arr in totalEdge:
            if (relax(arr, node[arr[1]])):
                node[arr[1]] = (node[arr[0]][0] + arr[2], arr[1])

    itr = itr + 1
    for arr in totalEdge:
        if (relax(arr, node[arr[1]])):
            return True

    return False


def negative_cycle(adj, cost):
    if (bellmanFord(adj, cost, 0)):
        return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
