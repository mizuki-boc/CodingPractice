K = int(input())
A, B = [int(a) for a in input().split()]
p = (A // K) * K
if (A <= p and p <= B) or (A <= p + K and p + K <= B):
    print("OK")
else:
    print("NG")