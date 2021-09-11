import sys 
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w') 
 
a = [] 
 
def func(x): 
    final = [] 
    for i in x: 
        for j in str(i): 
            if j != '-': 
                final.append(int(j)) 
    return sum(final) 
 
for i in range(int(input().split()[0])): 
    a.append([int(i) for i in input().split()]) 
 
a.sort(key=func) 
 
for i in range(len(a)): 
    for j in a[i]: 
        print(j, end=' ') 
    if i != len(a) - 1: 
        print('')
