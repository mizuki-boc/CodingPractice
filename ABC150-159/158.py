#A
# s = input()
# s1, s2 , s3 = s[0], s[1], s[2]
# if s1 != s2 or s1 != s3 or s2 != s3:
#     print("Yes")
# else:
#     print("No")

#B
# n, a, b = [int(_) for _ in input().split()]
# print((n // (a + b)) * a + min(n%(a+b), a))

#C
a, b = [int(_) for _ in input().split()]
p_a = a // 0.08
p_b = b // 0.10
print(p_a, p_b)
if p_a != p_b:
    print(-1)
else:
    print(min(p_a, p_b))

#D
