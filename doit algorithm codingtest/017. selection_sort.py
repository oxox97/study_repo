import sys
input = sys.stdin.readline

lst = [int(i) for i in list(input().strip())]  # sys.stdin.readline에서 개행문자 들어가서 strip()으로 제거

#print(lst)
for i in range(len(lst)-1):
    #print("\n>> i :", i)
    max_num = lst[i]
    max_index = i
    for j in range(i, len(lst)-1):
        #print("> j :", j)
        #print(lst[j], lst[j+1])
        if lst[j] < lst[j+1]:
            #print("# max changed")
            max_num = lst[j+1]
            max_index = j+1
    lst[i], lst[max_index] = lst[max_index], lst[i]
    #print(lst)
#print(lst)
for i in lst:
    print(i, end='')