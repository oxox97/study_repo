n = int(input())

lst = [int(input()) for _ in range(n)]

stack = []
lst_pointer = 0
answer = []
for i in range(1,n+1):
    answer.append("+")
    stack.append(i)
    while stack[-1]>=lst[lst_pointer]:  # while stack and stack[-1] == lst[lst_pointer]로 하면 더 간결!
        answer.append("-")
        stack.pop(-1)
        lst_pointer+=1
        if not stack:
            break
if len(stack):  # if stack
    print("NO")
else:
    for j in answer:
        print(j)