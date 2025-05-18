import sys
input = sys.stdin.readline

def check_dna(dna_dict, dna_condition):
    for key in dna_condition.keys():
        if dna_dict[key] < dna_condition[key]:
            return False  # 하나라도 틀리면 바로 False 반환
    return True

S, P = map(int, input().split())
DNA = input()
dna_condition = {key: val for key, val in zip("ACGT", map(int, input().split()))}  # 리스트 컴프리헨션 이용하여 input() 딕셔너리 만들기
dna_dict = {key: 0 for key in "ACGT"}

# 초기 윈도우
s = 0
e = P-1

for i in range(s, e+1):
    dna_dict[DNA[i]] += 1

cnt = 1 if check_dna(dna_dict, dna_condition) else 0

# 슬라이딩 윈도우
while e < S-1:
    dna_dict[DNA[s]] -= 1
    s += 1
    e += 1
    dna_dict[DNA[e]] += 1
    if check_dna(dna_dict, dna_condition):
        cnt += 1

 