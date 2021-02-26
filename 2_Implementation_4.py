data = ['2','1','B','A','D','3','7','A']

data.sort()
array = [0]*len(data)
sum = 0

for i, element in enumerate(data):
    if ord(element)<65:
        array[i] = 1
    else:
        array[i] = 0

for j in range(array.count(1)):
    sum += int(data[j])

result = [0]*(len(data)-array.count(1)+1)
result[-1] = str(sum)
result[0:-1] = data[array.count(1):] # 이거 마지막 까지 인덱싱 이렇게

result_character = '' #str으로 바로 눈으로 보이는 형태로 출력시키기 위한 빈 str
#result_character = [] # 이거 빈 리스트로 설정 해놓으면 어떻게 되지 ?
#빈리스트로 놓으면 되는 데 인덱싱이 안되네.

for k in result:
    result_character += k #문자하나씩 붙여쓰기 위해서 그냥 for문으로 물리적으로 더해줌.

print(result)
print(result_character)




