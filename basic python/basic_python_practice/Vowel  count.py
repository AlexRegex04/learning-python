x = 'zxcv vvtyzxcvbn mklj hgfdasqwer tyuuiioopoimv'
count = 0
for y in x:
    if y==" ":
        continue
    elif y=="a" or y=="e" or y=="i" or y=="o" or y=="u" or y=='A' or y=='E' or y=='I' or y=='O' or y=='U':
        count=count+1
         
print(count)
x = 'zxcv vvtyzxcvbn mklj hgfdasqwer tyuuiioopoimv'
count = 0
vowels = ['a','A','e','E','i','I','o','O','u','O']
for y in x:
    if y in vowels:
        count+=1
         
print(count)