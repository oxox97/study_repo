import sys
input = sys.stdin.readline

N, K = [int(i) for i in input().split()]
lst = [int(i) for i in input().split()]

def quick_sort(lst):

    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst)//2]

    low = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    high = [x for x in lst if x > pivot]

    return quick_sort(low) + middle + quick_sort(high)  # quick_sort(middle) 하면, 무한 루프 recursion

print(quick_sort(lst)[K-1])  # 실제 문제는 quick sort가 아닌 quick select (K만 찾으면 됨)

