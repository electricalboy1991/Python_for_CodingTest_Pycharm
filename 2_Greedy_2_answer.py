


n = 17
k =3


result = 0
count_1=0
while True:
    target = (n//k)*k
    count_1=n-target
    n=target
    if n<k:
        break
    n=n//k
    result = result+count_1 + 1

count_1+=(n-1)
result=count_1+result
print(result)

