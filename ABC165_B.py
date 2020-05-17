X = int(input())
bank = 100
year = 0
while bank < X:
    bank = bank * 101 // 100
    year += 1
print(year)