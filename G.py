import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# Решение задачи
input()

a = [int(i) for i in input().split()]

a.sort()

for i in a:
    print(i, end=" ")