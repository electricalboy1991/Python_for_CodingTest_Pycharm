N= 17
K = 3
count = 0
while N !=1:
    if N%K==0:
        N=N/K
        count=count+1
    else:
        N = N-1
        count=count+1
print(count)