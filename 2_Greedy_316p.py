def solution(food_times, k):
    turn = 0
    while k != 0:
        if list(set(food_times)) == [0]:
            answer =-1
            return answer

        if food_times[turn] >= 1:
            food_times[turn] -= 1
            turn += 1
            turn %= len(food_times)
            k -= 1
        else:
            turn += 1
            turn %= len(food_times)

    answer = turn + 1
    return answer

k = int(input())
food_times = list(map(int, input().split()))

print(solution(food_times, k))

