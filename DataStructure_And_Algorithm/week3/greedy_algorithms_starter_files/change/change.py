# Uses python3
import sys


def get_change(m):
    res = m // 10
    m = m % 10
    res = res + (m // 5)
    m = m % 5
    res = res + m
    return res


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
