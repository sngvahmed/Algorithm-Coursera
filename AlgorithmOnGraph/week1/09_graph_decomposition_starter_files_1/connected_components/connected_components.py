#Uses python3
# pylint: disable-msg=E1601
import sys

vis = [0] * 1000

def loopOnNode(adj, n):
    if(vis[n]):
        return
    vis[n] = 1
    for v in adj[n]:
        loopOnNode(adj, v)

def number_of_components(adj):
    result = 0
    for i in range(adj.__len__()):
        if(vis[i]):
            continue
        result += 1
        loopOnNode(adj, i)
    return result

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
    print(number_of_components(adj))
