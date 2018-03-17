#Uses python3
import sys


def max_dot_product(a, b):
    res = 0
    a, b = sorted(a), sorted(b)
    indxA, indxB = 0, 0

    for val in range(len(a)):
        if a[val] > 0:
            indxA = val
            break

    for val in range(len(b)):
        if b[val] > 0:
            indxB = val
            break

    ang, a, bng, b = a[:indxA], a[indxA:], b[:indxB], b[indxB:]
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    minR = min(len(a), len(b))
    for i in range(minR):
        res = res + (a[i] * b[i])

    minNg = min(len(ang), len(bng))
    for i in range(minNg):
        res = res + (ang[i] * bng[i])
    a, b = a[minR:], b[minR:]
    ang, bng = ang[minNg:], bng[minNg:]

    a = sorted(a + ang)
    b = sorted(b + bng)

    for i in range(len(a)):
        res = res + (a[i] * b[i])
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
