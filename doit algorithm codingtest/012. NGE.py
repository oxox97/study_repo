N = int(input())

lst = [int(i) for i in input().split()]
answer_list = []
stack = lst[::-1]

for i in range(N):
    top = stack.pop()
    print("top :", top)
    print("stack :", stack)
    while stack and stack[-1]<top:
        stack.pop()
    if stack:
        print(stack[-1])
    else:
        print(-1)

# for i in range(N):
#     queue = deque(lst[i+1:])
#     #print("i",lst[i])
#     #print(queue)
#     while queue and lst[i]>queue[0]:
#         queue.popleft()
#     if queue:
#         answer_list.append(queue[0])
#     else:
#         answer_list.append(-1)

# for a in answer_list:
#     print(a, end=' ')

    #print(-1)
    # stack = lst[i+1:]
    # while stack and lst[i] >= stack[-1]:
    #     stack.pop(-1)
    # try:
    #     print(stack[-1])
    # except:
    #     print(-1)
    # stack = lst.copy()

# for i in lst[::-1]:
#     stack.append(i)
#     if (stack) and (i < max(stack)):
#         answer_list.append(stack[0])
#     else:
#         answer_list.append(-1)

# print(answer_list, end=' ')

# for i in range(N):
#     queue = []
#     try:
#         a = [j for j in lst[i:N] if j > lst[i]][0]
#         print(a, end=" ")
#     except:
#         print(-1, end=" ")




#     for j in range(i+1,N):
#         if lst[i] < lst[j]:
#             queue.append(lst[j])
#     try:
#         answer_list.append(queue[0])
#     except:
#         answer_list.append(-1)

# for a in answer_list:
#     print(a, end=' ')