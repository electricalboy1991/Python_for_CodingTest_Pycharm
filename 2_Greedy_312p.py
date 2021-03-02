data = map(str, input().split())
data = list(''.join(data)) #


total_ing = int(data[0])
for i in range(1,len(data)):

    if int(data[i]) <= 1 or total_ing <= 1:
        total_ing=total_ing+int(data[i])
    else:
        total_ing=total_ing*int(data[i])
print(total_ing)
