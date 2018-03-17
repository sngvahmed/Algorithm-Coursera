# Uses python3
import sys
from random import randint


mem = {}
m = 1000007
def cfm(n):
    if n == 1 or n == 2:
        return 1

    if n in mem:
        return mem[n]

    k = n // 2
    if n % 2 == 0:
        mem[n] = ( (cfm(k)*cfm(k)) + (cfm(k-1)*cfm(k-1)) ) % 10
    else:
        mem[n] = ( (cfm(k)*cfm(k+1)) + (cfm(k-1)*cfm(k)) ) % 10

    return mem[n]

if __name__ == '__main__':
    mem[0], mem[1] = 1,1
    input = sys.stdin.read();
    n = int(input)
    print(cfm(n-1))
