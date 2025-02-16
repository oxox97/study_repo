import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
lst = [int(input()) for _ in range(N)]

iter = 0
distributed_lst = [deque() for i in range(10)]

for _ in range(len(str(max(lst)))):
    print("\n> iter :", iter)
    for i in lst:
        v = int(str(i//10**iter)[-1])
        print(v)
        if iter == 0:
            distributed_lst[v].append(i)
        else:
            distributed_lst
    print(distributed_lst)
    iter += 1

# queue = deque()

# 모르겠다 아래는 답
    
import sys
from collections import deque

# 빠른 입력 받기
input = sys.stdin.readline
N = int(input().strip())  # 숫자 개수
lst = [int(input().strip()) for _ in range(N)]  # 숫자 리스트

def radix_sort(arr):
    max_num = max(arr)  # 최댓값 확인 → 몇 자리 숫자인지 확인
    max_digits = len(str(max_num))  # 가장 긴 숫자의 자릿수

    for digit in range(max_digits):  # 각 자릿수에 대해 정렬 수행
        print(f"\n🚀 [Iter {digit}] 정렬 시작!")

        # 큐(버킷) 초기화 (0~9까지 10개의 큐)
        buckets = [deque() for _ in range(10)]

        # 해당 자릿수를 기준으로 큐에 분배
        for num in arr:
            digit_value = (num // (10 ** digit)) % 10  # 현재 자릿수의 숫자 추출
            buckets[digit_value].append(num)

        # 분배된 숫자들을 다시 리스트에 저장 (새로운 정렬된 리스트 생성)
        arr = []
        for i, bucket in enumerate(buckets):
            while bucket:
                arr.append(bucket.popleft())

        # 현재 상태 출력 (디버깅용)
        print("정렬된 리스트:", arr)

    return arr

# 실행 및 출력
sorted_lst = radix_sort(lst)
sys.stdout.write("\n".join(map(str, sorted_lst)) + "\n")
