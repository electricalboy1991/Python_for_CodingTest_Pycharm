import time
start = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(0, i):
        if array[i]< array[j]:
            picked = array.pop(i) #pop은 index로 뽑는 거임
            array.insert(j,picked) #insert쓰는 게 안좋다고 했는데.시간이 많이 들어서.
            # 근데 앞에서 부터 가는 게, 나한테는 직관적이라서,,,, 음.....
            break

end = time.time()

print(array)
print("Total time : ", end-start)
