n = int(input())

lst = [int(i) for i in input().split()]

max_score = max(lst)

new_lst = [j/max_score*100 for j in lst]

print(sum(new_lst)/n)

