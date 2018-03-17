# Uses python3
import sys
import random

def partition3(a, l, r):

    s, m, d = [], [], []
    m.append(a[l])
    for i in range(l + 1, r + 1):
        if a[i] == m[0]:
            m.append(a[i])
        elif a[i] > m[0]:
            d.append(a[i])
        else:
            s.append(a[i])
    newArr = s + m + d
    # print(a , newArr)
    c = 0
    for val in range(l, r + 1):
        a[val] = newArr[c]
        c = c + 1
    # print(a)

    return l + s.__len__(), r - d.__len__()


def randomized_quick_sort_partion3(a, l, r):
    if l >= r:
        return
    # print("------------")
    # print(l, r)
    m = partition3(a, l, r)
    # print(m)
    # print("------------")
    randomized_quick_sort_partion3(a, l, m[0] - 1);
    randomized_quick_sort_partion3(a, m[1] + 1, r);

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quick_sort_partion2(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort_partion2(a, l, m - 1);
    randomized_quick_sort_partion2(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # randomized_quick_sort_partion2(a, 0, n - 1)
    randomized_quick_sort_partion3(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
