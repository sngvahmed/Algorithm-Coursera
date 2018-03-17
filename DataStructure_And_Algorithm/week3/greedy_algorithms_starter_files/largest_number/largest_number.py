#Uses python3
import sys
from random import randint


def isBigger(left, right):
    lf, rt = str(left), str(right)
    for i in range(min(len(lf), len(rt))):
        if lf[i] > rt[i]:
            return True
        elif rt[i] > lf[i]:
            return False

    if len(lf) > len(rt):
        return True
    return False


def merge(left, right):
    res = []
    il, ir = 0, 0
    while len(left) > il or len(right) > ir:
        # print(il, ir, " = ", len(left), len(right), res)
        if il == len(left):
            res.append(right[ir])
            ir = ir + 1
        elif ir == len(right):
            res.append(left[il])
            il = il + 1
        else:
            if isBigger(left[il], right[ir]):
                res.append(left[il])
                il = il + 1
            else:
                res.append(right[ir])
                ir = ir + 1
    return res


def mergeSort(arr):
    if(len(arr) <= 1):
        return arr
    mid = int(len(arr) / 2)
    left = arr[:mid]
    right = arr[mid:]

    return merge(mergeSort(left), mergeSort(right))


def largest_number(a):
    a = mergeSort(a)
    res = ""
    for x in a:
        res += x
    return res


# file = open("input.txt", "w")
# for i in range(100):
#     n = randint(1, 1000)
#     arr = []
#     for i in range(n):
#         arr.append(randint(1, 1000))
#     file.write("{}\n".format(str(n)))
#     file.write("{}\n".format(' '.join(str(e) for e in arr)))
# file.close()
# print(sorted(arr, reverse=True))
# if sorted(arr, reverse=True).__eq__(mergeSort(arr)):
#     print("YES")
# else:
#     print("NO {}, {}".format(mergeSort(arr), mergeSort(arr)))
#     break

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
