import numpy as np

N = 8
l = {}

def printer(l):
    ar = np.zeros((N,N), dtype='int')
    
    for el in l:
        ar[el[0]][el[1]] = 1
        
    print ar
    
p = 0 if N%2 == 1 else 1
c = [x for x in range(N)]

while not len(l) == N:
    l[p] = c[0]
    c = c[1:]
    
    if N%2 == 0 and p == N-1:
        p = 0
    else:
        p = (p + 2)%N

l = sorted(l.items(), key=lambda x:x[0])

printer(l)