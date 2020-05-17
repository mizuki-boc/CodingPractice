#A
# n, m = [int(_) for _ in input().split()]
# print(int(n * (n - 1) / 2 + m * (m - 1) / 2))

#B
# def isReverse(s):
#     p1 = 0
#     p2 = len(s) - 1
#     flag = True
#     while p1 <= p2:
#         if s[p1] != s[p2]:
#             flag = False
#         p1 += 1
#         p2 += -1
#     return flag
# if __name__ == "__main__":
#     s = input()
#     s1 = s[:int((len(s) - 1) / 2)]
#     s2 = s[int((len(s) + 1) / 2):]
#     # print(s, s1, s2)
#     # print(isReverse(s), isReverse(s1), isReverse(s2))
#     if isReverse(s) and isReverse(s1) and isReverse(s2):
#         print("Yes")
#     else:
#         print("No")

#C
# l = int(input())
# a = b = c = l / 3
# print(a * b * c)

#D
# n = int(input())
# a = [int(_) for _ in input().split()]
# for k in range(len(a)):
#     ans = 0
#     popnum = a[0]
#     del a[0]
#     for i in range(len(list(set(a)))):
#         #print(a.count(list(set(a))[i]))
#         tmp = a.count(list(set(a))[i])
#         if tmp < 2:
#             pass
#         else:
#             ans += tmp * (tmp - 1) / 2
#     print(int(ans))
#     a.append(popnum)
def comb(s):
    return s * (s - 1) / 2
if __name__ == "__main__":
    n = int(input())
    a = [int(_) for _ in input().split()]
    c = 0
    for i in list(set(a)):
        c += comb(a.count(i))