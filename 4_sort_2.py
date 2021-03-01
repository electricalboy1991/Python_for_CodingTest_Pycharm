n, k = map(int, input().split()) # 이거는 리스트에 안 넣어도 되잖아 ?

raw_a = list(map(int, input().split()))
raw_b = list(map(int, input().split()))

raw_a.sort()
raw_b.sort(reverse=True)

for i in range(k):
    change_a = raw_a.pop(0)
    change_b = raw_b.pop(0)

    if change_a < change_b:
        raw_a.append(change_b)
        raw_b.append(change_a)
    else:
        break


print(sum(raw_a))
