# 다시 풀기
# 일단 이해하고 패스
# 2차원 구간합 외우면 될듯

n, m = [int(i) for i in input().split()]

lst = []
for _ in range(n):
    lst.append([int(i) for i in input().split()])
#print(f"lst : {lst}")

# sum_lst = [[0]*n]*n  # [0,0,0,0] 객체를 동일하게 4개 복사하기 때문에 하나를 바꾸면 모두 같은 리스트 객체 참조하게 됨ㅠ
# 따라서 하나 바꾸면 4개의 리스트 모두 값이 동일하게 바뀜 ..
sum_lst = [[0] * n for _ in range(n)]
#print(f"sum_lst : {sum_lst}\n")

for i in range(n):
    for j in range(n):
        if (i==0) and (j==0):
            sum_lst[i][j] = lst[0][0]
        elif i==0:
            sum_lst[i][j] = sum_lst[i][j-1] + lst[i][j]
        elif j==0:
            sum_lst[i][j] = sum_lst[i-1][j] + lst[i][j]
        else:    
            sum_lst[i][j] = sum_lst[i-1][j]+sum_lst[i][j-1]-sum_lst[i-1][j-1]+lst[i][j]
#print(sum_lst)

answer_lst = []
for k in range(m):
    s1,s2,e1,e2 = [int(i)-1 for i in input().split()]
    # print()
    # print(f"좌표 : {s1+1} {s2+1} {e1+1} {e2+1}")
    # print(sum_lst[e1][e2])
    # print("-",sum_lst[e1][s2-1])
    # print("-",sum_lst[s1-1][e2])
    # print("+",sum_lst[s1-1][s2-1])
    
    if (s1 == 0) and (s2 == 0):
        answer = sum_lst[e1][e2]
    elif s1 == 0:
        answer = sum_lst[e1][e2] - sum_lst[e1][s2-1]
    elif s2 == 0:
        answer = sum_lst[e1][e2] - sum_lst[s1-1][e2]
    else:
        answer = sum_lst[e1][e2] - sum_lst[e1][s2-1] - sum_lst[s1-1][e2] + sum_lst[s1-1][s2-1]
    answer_lst.append(answer)
    # print(answer)
    # print()

for answer in answer_lst:
    print(answer)