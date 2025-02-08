n = int(input())

lst = list(input())  # 숫자 한 자리씩 나누어 받기

lst = [int(i) for i in lst]

print(lst)

print(sum(lst))