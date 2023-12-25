batman = input("batman")
catman =  input("catman")
fatman = input("fatman")
friends = [batman,catman, fatman] 
cat_man_index = friends.index(catman)
print(cat_man_index)
print(friends[0])
print(type(friends))
print(friends.index(batman))
print(friends.index(fatman))
print(friends)
if batman=="batmen":
    prtint(batman)
elif batman=="catman":
    print("not catman")
elif batman=="fatman":
    print("not fatman")
else:
    print("dog")