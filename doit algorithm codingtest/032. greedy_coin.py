# 동전 조합 개수 최소화 문제
# 몫, 나머지 정리하는 대표적인 문제, 품!

N, K = [int(i) for i in input().split()]
coin_list = [int(input()) for _ in range(N)]

remaining_amount = K
coins = 0

for coin in sorted(coin_list, reverse=True):
    if remaining_amount == 0:
        break
    count = remaining_amount // coin
    remaining_amount -= coin * count  # remaining_amout %= coin
    coins += count

print(coins)

### 우선순위큐 사용 (heapq)

import heapq

N, K = map(int, input().split())
coins = [-int(input()) for _ in range(N)]  # 최대힙
heapq.heapify(coins)

remaining_amount = K
min_coins = 0

while remaining_amount > 0:
    coin = -heapq.heappop(coins)  # 가장 큰 동전 꺼내기 (-) 붙여서 나오기
    count = remaining_amount // coin
    remaining_amount %= coin
    min_coins += coin