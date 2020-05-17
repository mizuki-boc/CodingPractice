# #A
# N = input()
# if N[0] == "7" or N[1] == "7" or N[2] == "7":
#     print("Yes")
# else:
#     print("No")

#B
# N = int(input())
# A = list(range(1, N + 1))
# ans = 0
# for a in A:
#     if (a % 3 == 0) or (a % 5 == 0):
#         pass
#     else:
#         ans += A[a - 1]
# print(ans)

#C
def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
        
K = int(input())
ans = 0
for a in range(1, K+1):
    for b in range(a+1, K+1):
        for c in range(b+1, K+1):
            tmp = gcd(a, b)
            ans += gcd(tmp, c)
print(ans)
