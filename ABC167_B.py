#１行に複数の入力がある場合．（int）
A, B, C, K = (int(x) for x in input().split())
if A >= K:
    ans = K
else:
    ans = A
    tmp = K - A
    if B >= tmp:
        pass
    else:
        tmp = tmp - B
        ans += tmp * (-1)
print(ans)