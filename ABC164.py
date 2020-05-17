#A
S, W = [int(x) for x in input().split()]
if S > W:
    print("safe")
else:
    print("unsafe")

#B
A, B, C, D = [int(x) for x in input().split()]
run = True
while run:
    C -= B
    if C <= 0:
        run = False
        result = "Yes"
        continue
    A -= D
    if A <= 0:
        run = False
        result = "No"
        continue
print(result)

#C
N = int(input())
S = []
for i in range(N):
    S.append(input())
print(len(set(S)))

#D
# S = input()
# for i in range(S):
#     for j in range()