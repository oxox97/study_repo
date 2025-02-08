# 골드3임
# 일단 패스

N, M = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]
prefix_sum = [0]*(N+1)
for i in range(N):
    prefix_sum[i+1] = prefix_sum[i]+lst[i]

cnt = 0
for i in range(N):
    for j in range(i,N):
        a = prefix_sum[j+1] - prefix_sum[i]
        if a%3==0:
            cnt+=1
print(cnt)