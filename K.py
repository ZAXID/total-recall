import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
a = []
for i in range(int(input().split()[0])):
    a.append([int(i) for i in input().split()])
max = -9999
min = 9999
max_ind = -1
min_ind = 99999999999999999999999999999
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] >= max:
            max = a[i][j]
            max_ind = j
        if a[i][j] < min:
            min = a[i][j]
            min_ind = j
for i in range(len(a)):
    a[i][min_ind], a[i][max_ind] = a[i][max_ind], a[i][min_ind]
for i in range(len(a)):
    for j in a[i]:
        print(j, end=' ')
    if i != len(a) - 1:
        print('')
        