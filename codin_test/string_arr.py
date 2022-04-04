# https://www.acmicpc.net/problem/2941
import re
def solve2941():
    pattern = re.compile("c=|c-|dz=|d-|lj|nj|s=|z=")
    t = re.sub(pattern, "A", input())
    print(len(t))

solve2941()