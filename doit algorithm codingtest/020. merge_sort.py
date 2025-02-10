import sys
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

i = 0

def merge_sort(lst):
    global i
    i += 1
    #print("> i : ", i)
    #print(lst)

    if len(lst) == 1:
        return lst
    
    middle = len(lst)//2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)


def merge(left, right):  # 투포인터 사용할 수 있는 이유 : left와 right가 정렬된 상태여서 O(N)
    #print("l :", left)
    #print("r : ", right)
    i = 0  # i, j = 0, 0
    j = 0
    lst = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst.append(left[i])
            i += 1
        else:
            lst.append(right[j])
            j += 1
    lst += left[i:]
    lst += right[j:]
    #print("lst :", lst)
    return lst

for i in merge_sort(lst):
    print(i)

# print("\n".join(map(str, sorted_lst)) + "\n") ?
    
# 리스트 슬라이싱 대신 인덱스만 넘겨줘서 보다 빠른 코드 (선택)
# left = merge_sort(lst, start, middle)
# def merge_sort)lst, start, end):
#   if end - start <= 1:
#        return lst[start:end]   # 여기서 슬라이싱하면 O(1)이라 보다 효율적