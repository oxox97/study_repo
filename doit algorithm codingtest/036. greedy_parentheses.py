# questions = [
#     "55-50+40",  # -35
#     "10+20+30+40",  # 100
#     "00009-00009",  # 0
#     "30-40-50+20-10"  # -90 
# ]


q = input()

plus = sum(list(map(int, q.split('-')[0].split('+'))))
minus = sum([sum(list(map(int, i.split('+')))) if '+' in i else int(i) for i in q.split('-')[1:]])

a = plus - minus
print(a)