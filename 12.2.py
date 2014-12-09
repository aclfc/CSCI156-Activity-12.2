__author__ = 'Aidan'

L =[[1,2],[1,-1],[5,8],[-4,-2],[4,3]]
M = list()
for i in range(len(L)):
    tuple = (max(L[i]),(L[i]))
    M.append(tuple)
#print(M)
M.sort()
M.reverse()
#print(M)
for i in range(len(M)):
    L[i] = M[i][1]
print(L)

def mean(*args):
    c = len(args)
    sum = 0
    for i in range(c):
        sum += args[i]
    print("The mean is",(sum/c))
mean(1,2,3)