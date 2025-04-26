# 투 포인터
# 연속된 수들의 합 : sumtart_index와 end_idnex 같이 출발
# 알고리즘: 합이 기준보다 작으면, e+=1, sum+=e / 크면, sum-=s, s+=1
# (포인트) 연속된 숫자에선 인덱스가 곧 값이므로 리스트 생성 안하고 메모리 절약

import sys
input = sys.stdin.readline

N = int(input())

# 연속된 자연수이므로 리스트 만들 필요 없음 (메모리 절약)
s = 1
e = 1

cnt = 0
sum = 1
while s <= N and e <= N:  # s만 조건에 넣으면 됨
    # print(lisumt(range(s, e+1)), sum)
    if sum == N:
        cnt += 1
        sum -= s
        s += 1
    elif sum < N:
        e += 1
        sum += e
    else:
        sum -= s
        s += 1
print(cnt)