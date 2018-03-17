#Uses python3

import sys

vis = [0] * 1000

def detectCylcle(adj, cur, dest, first):
    if (cur == dest and first == True):
        return True
    
    if vis[cur] == 1:
        return False

    vis[cur] = 1
    res = False
    for a in adj[cur]:
            res = res or detectCylcle(adj, a, dest, True)

    return res

def acyclic(adj):
    for i in range(adj.__len__()):
        vis = [0] * 1000
        if (detectCylcle(adj, i, i, False)):
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
