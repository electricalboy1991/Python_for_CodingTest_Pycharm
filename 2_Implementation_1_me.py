n = input() # 기본으로 받는 값이 str 인듯.
data = list(map(str, input().split()))

x=1
y=1
temp_x=0
temp_y=0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

types_direction = ['E', 'W', 'S', 'N']

for my_direction in data:
    if my_direction=='E':
        temp_x = x + dx[0]
        temp_y = y + dy[0]
    elif my_direction=='W':
        temp_x = x + dx[1]
        temp_y = y + dy[1]
    elif my_direction=='S':
        temp_x = x + dx[2]
        temp_y = y + dy[2]
    else:
        temp_x = x + dx[3]
        temp_y = y + dy[3]

    if temp_x<1 or temp_y<1 or temp_x>n+1 or temp_y>n+1:
        temp_x = x
        temp_y = y
    else:
        x = temp_x # x = temp_x ,y = temp_y 이런식으로 하면 안된다고, 그냥 나열해서 쓰지마.
        y = temp_y

print(x,y)
