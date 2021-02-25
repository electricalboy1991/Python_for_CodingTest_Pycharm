rest = 1260
coin_list = [500, 100, 50, 10]
N_coin = [0]*4 #빈 리스트 만들기 이거 익숙해지기.

for i, coin in enumerate(coin_list):
    N_coin[i] = rest // coin
    rest = rest%coin
print(N_coin)