#Uses python3
# pylint: disable-msg=C0103,C0111,W0621
import sys

vis = [0] * 1000

def memsetObject(bufferObject):
    "Note, dangerous"
    import ctypes
    data = ctypes.POINTER(ctypes.c_char)()
    size = ctypes.c_int()  # Note, int only valid for python 2.5
    ctypes.pythonapi.PyObject_AsCharBuffer(ctypes.py_object(bufferObject), ctypes.pointer(data), ctypes.pointer(size))
    ctypes.memset(data, 0, size.value)

def reach(adj, x, y):
    if (x == y): 
        return True
    
    if(vis[x] == 1):
        return False

    vis[x] = 1

    res = False
    for v in adj[x]:
        res = (res or reach(adj, v, y))
    
    return res

if __name__ == '__main__':
    INPUT = sys.stdin.read()
    data = list(map(int, INPUT.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    if (reach(adj, x, y)):
        print(1)
    else:
        print(0)
