N, K = [int(x) for x in input().split()]
d = []
Snuke = [0] * N#最終的に0をもつインデックスがいたずらされる．
for k in range(K):
    d.append(input())
    A = [int(a) for a in input().split()]
    for a in A:
        Snuke[a - 1] += 1
count = 0
for i in Snuke:
    if i == 0:
        count += 1
print(count)
