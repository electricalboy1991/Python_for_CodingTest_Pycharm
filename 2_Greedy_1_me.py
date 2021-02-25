rest = 1260
coin_list = [500, 100, 50, 10]

index_500=0
index_100=0
index_50=0
index_10=0

while  rest!= 0:

    if rest>coin_list[0]:
        rest=rest-coin_list[0]
        index_500=index_500+1
    elif rest>coin_list[1]:
        rest=rest-coin_list[1]
        index_100 = index_100 + 1
    elif rest>coin_list[2]:
        rest=rest-coin_list[2]
        index_50 = index_50 + 1
    else:
        rest=rest-coin_list[3]
        index_10 = index_10 + 1

N_coins=[index_500,index_100,index_50,index_10]

print(N_coins)

##생각해보니 이걸 좀 바꿔봤어



