# Uses python3
import sys
import random


def optimal_weight(cap, arr, i, cur):
    if (cur > cap):
        return -1

    if i == arr.__len__():
        return cur
    # print(arr)
    sum = max(optimal_weight(cap, arr, i + 1, cur + arr[i]), optimal_weight(cap, arr, i + 1, cur))
    return sum;




if __name__ == '__main__':
    input = sys.stdin.read()
    capacity, n, *array = list(map(int, input.split()))

    mem = {}


    def optimized_weight(i, cur):
        if capacity < cur:
            return -1

        if (i, capacity - cur) in mem:
            return mem[(i, capacity - cur)]

        if i >= array.__len__():
            return cur

        mem[(i, capacity - cur)] = max(optimized_weight(i + 1, cur), optimized_weight(i + 1, cur + array[i]))
        return mem[(i, capacity - cur)]

    print(optimized_weight(0, 0))
    # print(optimized_weight(0, 0))
    # print(optimal_weight(W, w))
