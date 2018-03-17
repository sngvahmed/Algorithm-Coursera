# Uses python3
import sys

def initArray(starts , ends):
    arr = []
    for i in range(len(starts)):
        arr.append((starts[i], ends[i]))
    return sorted(arr)


def inBetween(val , arr):
    return arr[0] <= val and arr[1] >= val

def fast_count_segments(arr, points):
    arrIndx = 0
    res = []
    i = 0
    while i <len(points):
        val = points[i][0]
        
        if arrIndx == len(arr):
            # print("its exceeds")
            res.append(0)
            i = i + 1       
            continue

        # print(val , arr[arrIndx])
        if val < arr[arrIndx][0]:
            res.append(0)
            # print("appending 0")
            i = i + 1
            continue

        # print("not greating")

        if inBetween(val , arr[arrIndx]) == True:
            # print("its in inBetween")
            res.append(arrIndx + 1) 
        else:
            i = i - 1
            arrIndx += 1

        i = i + 1
    resInorder = [0] * len(res)
    # print(resInorder)
    # print(res, points)
    for i in range(len(res)):
        # print(points[i])
        resInorder[points[i][1]] = res[i]
    return resInorder

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    # print(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


def outPut(cnt):
    for x in cnt:
        print(x, end=' ')


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    a = data[2 * n + 2:]
    
    points = []

    for i in range(len(a)):
        points.append((a[i], i))
    points = sorted(points)
    # points, start, ends = changePointToPos(points, starts, ends)
    outPut(fast_count_segments(initArray(starts, ends), points))
    # outPut(naive_count_segments(starts, ends, a))
