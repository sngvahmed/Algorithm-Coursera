#!/usr/bin/env python3

import sys
from array import *

def distance(adj, s, t):
    vis = [0] * len(adj)
    q = []
    q.append((s,0))
    vis[s] = 1
    cnt = 0
    while(len(q) != 0):
        curNode = q[0]
        if (curNode[0] == t):
            return curNode[1]
        q.pop(0)
        vis[curNode[0]] = 1
        for v in adj[curNode[0]]:
            if (vis[v] == False):
                q.append((v,curNode[1] + 1))
        
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
