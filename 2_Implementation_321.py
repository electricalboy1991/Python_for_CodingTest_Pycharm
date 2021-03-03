score = input() # 기본으로 받는 값이 str 인듯.
indi_score = list(score)

num_num = len(indi_score)

left_sum = 0
right_sum = 0

for i in range(int(num_num/2)):
    left_sum +=int(indi_score[i])

for j in range(int(num_num/2),num_num):
    right_sum +=int(indi_score[j])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')