# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):

    segments = sorted(segments)

    x, y = segments[0][0], segments[0][1]
    ranges = [(int(x), int(y))]
    curIndx = 0
    for i in range(1, len(segments)):
        if int(segments[i][0]) > int(ranges[curIndx][1]):
            ranges.append((int(segments[i][0]), int(segments[i][1])))
            curIndx = curIndx + 1
        else:
            ranges[curIndx] = (max(int(ranges[curIndx][0]), int(segments[i][0])), min(ranges[curIndx][1], segments[i][1]))
    res = []
    for vl in ranges:
        res.append(vl[0])
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
