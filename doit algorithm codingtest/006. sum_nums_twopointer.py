# 다시 풀어보기
# 연속된 수들의 합 수 찾기 - 투 포인터
# 개념
# start_index와 end_index 같이 출발
# lst[start_index:end_index]의 합이 기준보다
# 작으면, end_index++, 크면 start_index++
# (중요) current_sum 이용하여 계속 sum 안 하게 메모리 관리 (리스트 생성 없이, 여기선 인덱스가 곧 값..)


N = int(input())

#lst = [int(i) for i in range(1,N+1)]

start_index = 1
end_index = 1
current_sum = 1
# answer_list = []
cnt = 0


while end_index <= N:
    if current_sum == N:
        # answer_list.append([i for i in range(start_index+1,end_index+1)])
        cnt += 1
        current_sum -= start_index
        start_index += 1
    elif current_sum > N:
        current_sum -= start_index
        start_index += 1
    else:
        end_index += 1
        current_sum += end_index

#print(answer_list)
print(cnt)



# 구간 합 이용하여 푼 나의 코드 (O(N^2))
"""
N = int(input())

lst = [int(i) for i in range(1,N+1)]
prefix_sum = [0] * (N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + lst[i]

answer_list = []
for i in range(N):
    for j in range(i+1,N+1):
        a = prefix_sum[j] - prefix_sum[i]
        if a > N:
            break
        if a == N:
            answer_list.append([i,j])

print(len(answer_list))
"""


# 얘도 lst[start_index:end_index+1] 인덱스 생성 때문에 O(N^2)
"""

N = int(input())

lst = [int(i) for i in range(1,N+1)]

start_index = 0
end_index = 0
answer_list = []

while start_index < N:
    s = sum(lst[start_index:end_index+1])
    if s == N:
        answer_list.append([i for i in range(start_index+1,end_index+2)])
        start_index += 1
    elif s > N:
        start_index += 1
    else:
        end_index += 1

print(len(answer_list))
"""