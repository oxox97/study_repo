# 구간 합 핵심 문제 (실버3)
# 다시 풀기
# O(N+M)

N, M = [int(i) for i in input().split()]

lst = [int(i) for i in input().split()]
gugan = [[int(i) for i in input().split()] for _ in range(M)]

prefix_sum = [0] * (N+1)  # PEP 8 스타일에서 연산 시 양옆에 공백 넣는 것 권장
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i] + lst[i]

answer_list = []
for g in gugan:
    s,e = g[0], g[1]
    a = prefix_sum[e] - prefix_sum[s-1]
    answer_list.append(a)

# 인덱스 0 추가 -> 하나씩 밀림
# 문제에서 0번째가 아닌, 1번쨰가 처음 -> 인덱스가 당겨짐
# 결국 같아짐. 헷갈리는데 이해 완료 (그냥 외워)

for a in answer_list:
    print(a)




"""
# 이전 노력

n, q = [int(i) for i in input().split()]
lst = [int(j) for j in input().split()]

sum_lst = [lst[0]]
for i in range(1,n):
    sum_lst.append(sum_lst[i-1] + lst[i])

answer = []
for j in range(q):
    start, end = [int(i)-1 for i in input().split()]
    if start > 0:
        answer.append(sum_lst[end]-sum_lst[start-1])
    else:
        answer.append(sum_lst[end])

for k in answer:
    print(k)

"""
    

# 다시 풀기

# n, m = [int(i) for i in input().split()]
# lst = [int(i) for i in input().split]

"""
n = 5
m = 3
lst = [5,4,3,2,1]

prefix_sum = [0] * (n+1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + lst[i]

print(prefix_sum)

s = 5
e = 5
answer = prefix_sum[e] - prefix_sum[s-1]

print(answer)
"""