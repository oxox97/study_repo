N = int(input())

lst = [int(input()) for i in range(N)]
lst2 = []

for i in lst:
    if i!=0:
        lst2.append(i)
    else:
        if len(lst2)==0:
            print(0)
        else:
            min_abs = min([abs(j) for j in lst2])
            a = min([i for i in lst2 if abs(i)==min_abs])
            print(a)
            lst2.remove(a)
