data = map(int, input().split())
sorted_data = sorted(data) #이거 매서드 외워야지.

result = 0
count = 0

for i in sorted_data:
    count +=1
    if i > count:
        continue
    else:
        result+=1
        count = 0

print(result)



