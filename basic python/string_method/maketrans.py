
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

txt = "Good good god gd dg Sam!"
x = "good"
y = "xoyf"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "I could eat bananas all day, bananas are my favorite apples fruit"
x = txt.rpartition("apples")
print(x)

txt = "apple, banana, cherry"
x = txt.rsplit(", ", 1)
print(x)

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)  # Hello B2B2B2 And 3G3G3G

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)  # hELLO mY nAME iS peter


txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

txt = "Thank you for the music\nWelcome to the jungle"
# ['Thank you for the music\n', 'Welcome to the jungle']
x = txt.splitlines(True)
# ['Thank you for the music', 'Welcome to the jungle']
x = txt.splitlines()
print(x)

txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(".,wqsanb")
print(x)

