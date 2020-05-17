#A
R = int(input())
print(2 * R * 3.14)

#B
N, M = [int(x) for x in input().split()]
A = [int(a) for a in input().split()]
tmp = N - sum(A)
if tmp >= 0:
    print(tmp)
else:
    print(-1)

#C
N = int(input())
A = [int(a) for a in input().split()]
ans = [0] * N
for i in A:
    ans[i-1] += 1
for result in ans:
    print(result, "\n")

# #D
# N, K = [int(x) for x in input().split()]
# num = [10 ** 100] * (N + 1)