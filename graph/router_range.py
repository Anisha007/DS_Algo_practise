"""
A:(0,0)
B:(0,0)
"""
import math


def isReachable(a, b, rng, location):
    x1, y1 = location[a]
    x2, y2 = location[b]

    dist = math.sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2)
    if dist <= rng:
        return True
    else:
        return False


def solve(src: str, desc: str, location: dict[(int, int)], rng) -> bool:
    queue = [src]
    visited = set()
    visited.add(src)

    while len(queue):
        a = queue.pop(0)
        for b in location.keys():
            if b == a or b in visited:
                continue
            if isReachable(a, b, rng):
                queue.append(b)
                visited.add(b)

    if desc in visited.keys():
        return True
    else:
        return False
