import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def compareX(a, b):
    p1 = a
    p2 = b
    return (p1.x - p2.x)


def compareY(a, b):
    p1 = a
    p2 = b
    return (p1.y - p2.y)

def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y))


def bruteForce(P, n):
    min_dis = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_dis:
                min_dis = dist(P[i], P[j])
    return min_dis


def min(x, y):
    return x if x < y else y


def stripClosest(strip, size, d):
    min_dist = d
    strip = sorted(strip, key=lambda point: point.y)
    for i in range(size):
        for j in range(i + 1, size):
            if (strip[j].y - strip[i].y >= min_dist):
                break
            if dist(strip[i], strip[j]) < min_dist:
                min_dist = dist(strip[i], strip[j])
    return min_dist


def closestUtil(P, n):
    if n <= 3:
        return bruteForce(P, n)
    mid = n // 2
    midPoint = P[mid]
    dl = closestUtil(P, mid)
    dr = closestUtil(P[mid:], n - mid)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(P[i].x - midPoint.x) < d:
            strip.append(P[i])
    return min(d, stripClosest(strip, len(strip), d))


def closest(P, n):
    P = sorted(P, key=lambda point: point.x)
    return closestUtil(P, n)


P = [Point(x=3, y=2), Point(x=10, y=20), Point(x=4, y=5), Point(x=20, y=30), Point(x=10, y=12), Point(x=50, y=10)]
n = len(P)
print("Smallest distance is: ", closest(P, n))
