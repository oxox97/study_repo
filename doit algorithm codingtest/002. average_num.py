import sys
input = sys.stdin.readline

N = int(input())

scores = list(map(int, input().split()))

# print(scores)

M = max(scores)

adjusted_scores = [s/M*100 for s in scores]

print(sum(adjusted_scores)/N)