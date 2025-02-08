# 다시 풀기
# 양 끝단에서 시작하는 거 간단한데 생각 못 했다..
# 중간에서 시작하면 일부 조합 못 찾음
# 투 포인터는 반드시 끝 단에서 시작!!!

N = int(input())
M = int(input())

lst = sorted([int(i) for i in input().split()])

s = 0
e = N-1
current_sum = 0
answer_list = []

while s < e:
    current_sum = lst[s] + lst[e]
    if current_sum == M:
        answer_list.append([s,e])
        s += 1
        e -= 1
    elif current_sum < M:
        s += 1
    else:
        e -= 1


print(len(answer_list))
