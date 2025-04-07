T = int(input())

q_list = [list(map(int, input().split())) for _ in range(T)]

def GCD(A, B):
    while True:
        a = max(A, B) % min(A, B)
        if a == 0:
            return min(A, B)
        else:
            A = min(A, B)
            B = a

def GCD_answer(A, B):
    while b > 0:
        a, b = b, a % b
    return a

for A, B in q_list:
    answer = A * B // GCD(A, B)
    print(answer)

# math.gcd(A, B)도 사용 가능