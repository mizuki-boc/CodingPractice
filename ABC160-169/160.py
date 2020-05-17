#A
# s = input()
# if s[2] == s[3] and s[4] == s[5]:
#     print("Yes")
# else:
#     print("No")

#B
# x = int(input())
# y500 = x // 500
# y5 = (x - 500 * y500) // 5
# print(y500 * 1000 + y5 * 5)

#C
# k, n = [int(_) for _ in input().split()]
# a = [int(_) for _ in input().split()]
# b = []
# for i in range(len(a)):
#     if i == 0:
#         b.append(k - a[len(a) - 1] + a[0])
#     else:
#         b.append(a[i] - a[i - 1])
# print(k - max(b))

#D
n, x, y = [int(_) for _ in input().split()]
g = list(range(1, n+1))
for i in range(n - k):#はじまり
    for p in range(k):#グラフ　1+p から 1+p+k が考えてるグラフ(not 1+p<x<1+p+k)
        if i + p <= x and x <= 1 + p + k:
            pass
            #この場合はxy間で最短経路が更新されるばあいがある．