#!/usr/bin/env python3
#Uses python3

import sys
import queue

from heapq import *

def bellmanFord(adj, cost, s, t):
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

    cont = True
    while (cont):
        cont = False
        for arr in totalEdge:
            if (relax(arr, node[arr[1]])):
                cont = True
                node[arr[1]] = (node[arr[0]][0] + arr[2], arr[1])

    if (node[t][0] == sys.maxsize):
        return -1
    return node[t][0]


def dijkstra(adj, cost, s, t):
    vis = []
    prev = []
    heap = queue.PriorityQueue()

    for i in range(0, adj.__len__()):
        vis.append(sys.maxsize)
        prev.append(None)
        if (i == s):
            heap.put([0, s])
        else:
            heap.put([sys.maxsize, s])


    while not heap.empty():

        o = heap.get()

        for i in range(0, adj[o[1]].__len__()):
            goNode = adj[o[1]][i]
            goCost = cost[o[1]][i]

            if (vis[goNode] > (o[0] + goCost)):
                vis[goNode] = o[0] + goCost
                prev[goNode] = o[1]
                heap.put([o[0] + goCost, adj[o[1]][i]])

    if (vis[t] == sys.maxsize):
        return -1
    return vis[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(dijkstra(adj, cost, s, t))
