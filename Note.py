# Python の内包表記
#たとえば，
ans = []
for i in range(10):
    ans.append(i ** 2)
#としたいとき，
ans2 = [x ** 2 for x in range(10)]
#でおk
