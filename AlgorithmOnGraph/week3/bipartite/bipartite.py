#!/usr/bin/env python3

import sys
import queue    

def bipartite(adj):
    vis = [0] * len(adj)
    q = []

    for v in range(0,len(adj)):
        if (vis[v] == 0):
            q = []
            q.append((v,1))
            vis[v] = 1
            while(len(q) != 0):
                node = q[0]
                q.pop(0)

                for l in adj[node[0]]:
                    if (vis[l] == 0):
                        if (node[1] == 1):
                            vis[l] = 2
                            q.append((l,2))
                        else:
                            vis[l] = 1
                            q.append((l,1))
                    else :
                        if (vis[l] == node[1]):
                            return 0
    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
