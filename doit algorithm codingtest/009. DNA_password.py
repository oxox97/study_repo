# 계속 시간 초과 일단 패스
# 얻어갈 것
# 1) from collections import defaultdict / dict = defaultdict(int) : 초기화 자동 (keyerror 방지)
# 2) count 비효율? 맞나? 그냥 for문으로 함
# 3) flag = False 뜨면 바로 break
# 4) 투 포인터 개념 이해 완료

import sys
from collections import defaultdict

input = sys.stdin.readline

P, S = [int(i) for i in input().split()]
dna = input()
dna_dict = {}
for d, n in zip(['A', 'C', 'G', 'T'],[int(i) for i in input().split()]):
    dna_dict[d] = n
current_dict = defaultdict(int)

s = 0
e = S

#for d, n in dna_dict.items():
#    current_dict[d] = dna[s:e].count(d)  # count는 비효율이래. defulatdict 이용해서 초기 할당해주기
for i in range(S):
    current_dict[dna[i]] += 1

#answer_list = []
cnt = 0
while e <= P:
    #print("> s :", s, "/ e :", e)
    #print("> dna[s:e] : ", dna[s:e])
    flag = True
    for d, n in dna_dict.items():
        if current_dict[d] < dna_dict[d]:
            flag = False
            break  # false면 바로 나가기
    if flag:
        #answer_list.append(dna[s:e])
        cnt += 1
    
    if e < P:
        #print("---투 포인터 이동--")
        current_dict[dna[s]] -= 1
        current_dict[dna[e]] += 1  # [s:e+1][-1] == dna[e] ...
        s += 1
        e += 1
#        current_dict[dna[s:e][0]] -= 1
#        s += 1
#        e += 1
#        current_dict[dna[s:e][-1]] += 1
#print(answer_list)
#print(len(answer_list))
print(cnt)


# 내가 푼 시간 초과 로직
# 문제 : 반복문 아넹서 lst.count('A')는 len(lst)만큼 시간 필요 (=O(S))
# 따라서 반복문 안에서 투포인터 이용해야 함

"""
import sys
input = sys.stdin.readline

P, S = [int(i) for i in input().split()]
dna = input()
dna_dict = {}
for d, n in zip(['A', 'C', 'G', 'T'],[int(i) for i in input().split()]):
    dna_dict[d] = n

answer_list = []
for i in range(P-S+1):
    a = dna[i:i+S]
    print(a)
    flag = True
    for d, n in dna_dict.items():
        if a.count(d) < n:  # O(S) 연산이므로, P-S+1 번 반복하면 O(P*S)가 되어서 시간 초과됨
            flag = False
    if flag:
        answer_list.append([a])

print(answer_list)
print(len(answer_list))
"""