# key point : "리스트 슬라이싱"이 아닌, "인덱스 기반 탐색" : left, right 인덱스 사용하여 탐색 범위 조절 (메모리 효율적)
# 변수는 mid

"""
import sys
sys.setrecursionlimit(100000)

N = int(input())

lst = sorted([int(i) for i in input().split()])

M = int(input())

question = [int(i) for i in input().split()]

def binary_search(q, lst, left, right):  # lst, left, right
    if left > right:
        return 0
    median_index = (left + right) // 2
    median = lst[median_index]
    # print("lst :", lst)
    # print("median :", median)
    
    if q == median:
        return 1
    #if len(lst) == 1:
    #    return 0
    elif q > median:
        # lst = lst[median_index:]  # 이렇게 슬라이싱하면 시간 초과
        return binary_search(q, lst, median_index + 1, right)  # ⭐️ 여기 리턴 해야 함! (1,0을 최상위 함수로 전달하기 위해)
    else:
        # lst = lst[:median_index]
        return binary_search(q, lst, left, median_index-1)  # ⭐️ 여기 리턴 해야 함!

for q in question:
    print(binary_search(q, lst, 0, N-1))  # 처음엔 전체

"""

# binary search 정리 및 다시 개념 정리

N = int(input())
lst = sorted([int(i) for i in input().split()])
M = int(input())
question = [int(i) for i in input().split()]

# 방법 1. 범위 절반씩 줄이기 (two-pointer는 동시에 모아지는걸로 다르다고 함)
def binary_search(lst, q, left, right):
    # print("> q:", q)
    while left <= right:
        median_index = (left + right) // 2
        median = lst[median_index]
        # print(median)

        if median == q:
            return 1
        elif median > q:
            right = median_index - 1
        elif median < q:  # else 동일
            left = median_index + 1
    return 0

# for q in question:
#     print(binary_search(lst, q, 0, len(lst)-1))

# 방법 2. recursion

import sys
sys.setrecursionlimit(100000)

def binary_search_recursion(lst, q, left, right):
    if left > right:
        return 0  # 기저 조건 (Base Case)
    
    median_index = (left + right) // 2
    median = lst[median_index]

    if median == q:
        return 1
    elif median > q:
        return binary_search_recursion(lst, q, left, median_index-1)
    else:
        return binary_search_recursion(lst, q, median_index+1, right)

for q in question:
    print(binary_search_recursion(lst, q, 0, len(lst)-1))