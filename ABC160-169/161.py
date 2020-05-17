#A
# x, y, z = [int(_) for _ in input().split()]
# x, y = y, x
# x, z = z, x
# print(x, y, z)

#B
# n, m = [int(_) for _ in input().split()]
# a = [int(_) for _ in input().split()]
# total = sum(a)
# th = 1 / (4 * m) * total
# import numpy as np
# A = np.array(a)
# A_sorted = A.argsort()[::-1]
# # 上からM個選ぶ
# if A[A_sorted[m - 1]] < th:
#     print("No")
# else:
#     print("Yes")

#C
# n, k = [int(_) for _ in input().split()]
# n = n % k
# if abs(n - k) < n:
#     print(abs(n -k))
# else:
#     print(n)

#D
# k = int(input())
# q = [1,2,3,4,5,6,7,8,9]
# count = 0
# if k <= 9:
#     print(k)
# else:
#     while not count == k:
#         count += 1
#         x = q.pop(0)
#         if x % 10 == 9:
#             q.append(x * 10 + x % 10 -1)
#             q.append(x * 10 + x % 10)
#         elif x % 10 == 0:
#             q.append(x * 10 + x % 10)
#             q.append(x * 10 + x % 10 + 1)
#         else:
#             q.append(x * 10 + x % 10 - 1)
#             q.append(x * 10 + x % 10)
#             q.append(x * 10 + x % 10 + 1)
#     print(x)

#E
n, k, c = [int(_) for _ in input().split()]
s = input()
ans = []
for i in range(len(s)):#働き始めるとき
    tmp = []
    bef = -1#前働いた時
    for j in range(i, len(s)):
        if s[j] == "o":
            if (j - bef >= c + 1 or bef == -1) and len(tmp) < k:
                #働く
                tmp.append(j)
                bef = j
            else:
                #働かない
                pass
        elif s[j] == "x":
            #働かない
            pass
    if len(tmp) == k:
        ans.append(tmp)
for i in range(len(ans) - 1):
    res = set(ans[i]) & set(ans[i + 1])
    print(res)
res = list(res).sort()
for i in range(len(res)):
    print(res[i])