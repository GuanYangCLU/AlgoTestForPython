# https://www.hackerrank.com/challenges/queens-attack-2/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obsTuple = set([(ob[0], ob[1]) for ob in obstacles])
    if outOfBound(r_q, c_q, n):
        return 0
    direct = [(1, 0), (-1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, -1)]
    pos = (r_q, c_q)
    queue = collections.deque([(direct, pos)])
    res = -1
    while queue:
        newDirect, newPos = queue.popleft()
        x, y = newPos
        if isValid((x, y), n, obsTuple):
            res += 1
            for d in newDirect:
                queue.append(([d], (x + d[0], y + d[1])))
    return res
    
def isValid(pos, n, obsTuple):
    if outOfBound(pos[0], pos[1], n):
        return False
    return pos not in obsTuple
    
def outOfBound(x, y, n):
    return x < 1 or x > n or y < 1 or y > n
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
