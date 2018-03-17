# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

a = sorted(a)

print(a[len(a) - 1] * a[len(a) - 2])
