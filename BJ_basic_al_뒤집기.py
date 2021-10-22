import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    string = list(input().split())
    for j in string:
        print(j[::-1], end=' ')