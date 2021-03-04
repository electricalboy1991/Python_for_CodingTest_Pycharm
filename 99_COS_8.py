
# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(garden):
    n = len(garden)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    direction = ['E' ,'W' ,'S' ,'N']
    list_sum =0
    answer = 0
    temp_garden= garden

    while 1:
        for i in range(n):
            list_sum += sum(garden[i][:])

        if list_sum == n* n:
            break
        else:
            list_sum = 0

        for i in range(n):
            for j in range(n):
                if garden[i][j] == 1:
                    for k in range(len(direction)):
                        # 가용 범위가 아닐 때
                        if i + dx[k] <= -1 or i + dx[k] >= n or j + dy[k] <= -1 or j + dy[k] >= n:
                            continue
                        else:
                            temp_garden[i + dx[k]][j + dy[k]] = 1

        answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

