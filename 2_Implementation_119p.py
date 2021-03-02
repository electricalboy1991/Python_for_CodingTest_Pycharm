n,m = map(int, input().split()) # 기본으로 받는 값이 str 인듯.
pos_x, pos_y, now_direction =map(int, input().split())

map_data = [[0]*m for _ in range(n)]

for i in range(n):
    map_data[i][:] = list(map(int, input().split())) #map은 예약어니까 변수로 쓰면 안되지

map_data[pos_x][pos_y] = 2
way_direction={ 0 :[0, -1], 1 :[-1,0], 2 :[0,1], 3:[1,0]}
back_direction={ 0 :[1, 0], 1 :[0,-1], 2 :[-1,0], 3:[0,1]}

around = map_data[pos_x-1][pos_y] and map_data[pos_x][pos_y-1] and map_data[pos_x+1][pos_y] and map_data[pos_x][pos_y+1]

num_visit = 1
while around == 0:
    # 바라보고 있는 방향에 따른 첫 이동 후보군 선정
    for j in range(4):
        if now_direction==j:
            temp_x = pos_x + way_direction[j][0]
            temp_y = pos_y + way_direction[j][1]
        else:
            continue

    if map_data[temp_x][temp_y] == 0:
        pos_x = temp_x
        pos_y = temp_y
        map_data[temp_x][temp_y] = 2 # 방문처리
        num_visit += 1

    else:

        if around == 1:
            for k in range(4):
                if now_direction == k:
                    pos_x = pos_x + back_direction[k][0]
                    pos_y = pos_y + back_direction[k][1]
                else:
                    continue

            if map_data[pos_x][pos_y ] ==1:
                continue  # 여기로 나오면 끝나지

        if now_direction ==0:
            now_direction = 3
        else:
            now_direction -=1
        continue # 임시로 갈 길을 다시 정해보는 continue

print(num_visit)
