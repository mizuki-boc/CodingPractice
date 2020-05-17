"""
#input関数で入力文字を取得する
str = input().split()#split()で空白区切りで文字の分割が可能．split("/")とかもできる，
print(str)
s = [input() for i in range(3)]#これで複数行の入力を代入できる．
print(s)
"""
flag = True
s = [input() for i in range(2)]
if (len(s[0]) > 10 or len(s[0]) < 1) or (len(s[0]) + 1 != len(s[1])):
    flag = False
else:
    for j in range(len(s[0])):
        if not s[0][j] == s[1][j]:
            flag = False
if flag:
    print("Yes")
else:
    print("No")
#出力文字が大文字，小文字とかもちゃんと判断される．今回 print("yes") としてて間違いになった．