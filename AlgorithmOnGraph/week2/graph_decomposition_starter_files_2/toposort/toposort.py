#Uses python3

import sys

vis = [0] * 100001
result = []
res = []
adj = []

def dfs(x):
    vis[x] = 1
    
    for node in adj[x]:
        if vis[node] == 0:        
            dfs(node)
    
    res.insert(0,x)
    
    
def toposort(adj):
    for v in range(adj.__len__()):
        if(vis[v] == 0):
            dfs(v)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    toposort(adj)
    for x in res:
        print(x + 1, end=' ')
        # print(x , end=' ')

