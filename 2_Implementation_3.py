data_raw = list(input())        # map 함수에 대한 공부 int라는 함수에 iterable 자료형을 넣는 거임
# 이거 리버스 하는 거 암기하기 data_raw.reverse()

dic = {'a':1, 'b':2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
# 딕셔너리 쓰는 법 -> {} 사전이니까 저런 기호 쓰는 거라고.

print(data_raw)


data = [int(data_raw[1]), int(dic[data_raw[0]])]
# dictionary에서 key 찾아서 쓸 때, []에 넣어서 찾는다. 구멍에 넣듯이.
# data int로 바꿔주는 거 보기

count = 0

if data[0]-2>0 and data[1]-1>0:
    count+=1
if data[0]-1>0 and data[1]-2>0:
    count+=1
if data[0]-2>0 and data[1]+1<9:
    count+=1
if data[0]-1>0 and data[1]+2<9:
    count+=1
if data[0]+1<9 and data[1]+2<9:
    count+=1
if data[0]+2<9 and data[1]+1<9:
    count+=1
if data[0]+2<9 and data[1]-1>0:
    count+=1
if data[0]+1<9 and data[1]-2>0:
    count+=1

print(count)
