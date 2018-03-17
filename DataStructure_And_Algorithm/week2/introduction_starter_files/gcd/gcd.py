# Uses python3
import sys
from random import randint


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


def stress_test():
    for _ in range(10000):
        rn1, rn2 = randint(1, 10000), randint(1, 10000)
        ans1, ans2 = gcd_naive(rn1, rn2), gcd(rn1, rn2)
        if ans1 == ans2:
            print("YES")
        else:
            print("WA ", ans1, ans2, "value= ", rn1, rn2)
            break

if __name__ == "__main__":
    # stress_test()
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
