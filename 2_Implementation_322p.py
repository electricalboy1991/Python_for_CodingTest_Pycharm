data = input() # 기본으로 받는 값이 str 인듯.

sorted_data=sorted(data)
result = []
num = 0

for i in range(len(sorted_data)):
    if ord(sorted_data[i])>=ord('A'):#알파벳
        result.append(sorted_data[i])
    else:
        num +=int(sorted_data[i])

result.append(str(num))
print(''.join(result))
