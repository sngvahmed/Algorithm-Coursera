# Uses python3
import sys

def get_majority_element(a):

    arr = {}
    for val in a:
        if val in arr:
            arr[val] = arr[val].__add__(1)
        else:
            arr[val] = 0
    for val in a:
        if arr[val] >= int(len(a) // 2):
            return 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
