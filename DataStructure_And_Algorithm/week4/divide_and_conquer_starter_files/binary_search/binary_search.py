# Uses python3
import sys


def binary_search(a, x , st, end):

    if st.__eq__(end):
        if a[st - 1] != x:
            return -1
        return st - 1

    mid = (st + end)//2
    if x > a[mid - 1]:
        return binary_search(a, x, mid + 1, end)
    else:
        return binary_search(a, x, st, mid)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x, 1, len(a)), end = ' ')
        # print("{} , {}".format(binary_search(a, x, 1, len(a)), linear_search(a, x)))
