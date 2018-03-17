# Uses python3
import sys


def calculateInversion(a, left, ave, right):
    a1 = sorted(a[left:ave+1])
    a2 = sorted(a[ave+1:right+1])
    res = 0
    i, j = 0, 0
    q = left
    # print(a1, a2)
    while (i < len(a1)) or (j < len(a2)):
        if i == len(a1):
            a[q] = a2[j]
            q, j = q + 1, j + 1
        elif j == len(a2):
            a[q] = a1[i]
            q, i = q + 1, i + 1
        else:
            if a1[i] <= a2[j]:
                a[q] = a1[i]
                i = i + 1
            else:
                a[q] = a2[j]
                # print((len(a1) - i))
                res = res + (len(a1) - i)
                j = j + 1
            q = q + 1
    return res

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right <= left:
        return number_of_inversions
    
    ave = (left + right) // 2

    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave + 1, right)
    res = calculateInversion(a, left, ave, right)
    # print(res)
    number_of_inversions += res
    # print( "============ {} ==========".format(a))
    return number_of_inversions


def merge_sort(a):
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(max(0, get_number_of_inversions(a, 0, len(a)-1)))
