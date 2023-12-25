Months = set(["January", "February", "March", "April", "May", "June"])
# Adding items to the set
Months.add("July")
# update() function
Months.update(('August',))

# Python Set Operations
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday", "Sunday"}
Days2 = {"Friday", "Saturday", "Sunday"}
print(Days1 | Days2)  # printing the union of the sets
# using union() method

Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Friday", "Saturday", "Sunday"}
print(Days1.union(Days2))  # printing the union of the sets
# Intersection of two sets


# Using & operator
Days1 = {"Monday", "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday", "Friday"}
print(Days1 & Days2)  # prints the intersection of the two sets
# Using intersection() method
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {1, 2, 20, 32, 5, 9}
set3 = set1.intersection(set2)
print(set3)

# Difference between the two sets
# Example 1 : Using subtraction ( - ) operator
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1-Days2)  # {"Wednesday", "Thursday" will be printed}
# Using difference() method
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday", "Sunday"}
print(Days1.difference(Days2))  # prints the difference of the two

# Symmetric Difference of two sets
'''দুটি সেটের সিমেট্রিক পার্থক্য ^ অপারেটর বা symmetric_difference() পদ্ধতি দ্বারা গণনা করা হয়। সেটের সিমেট্রিক পার্থক্য, এটি সেই উপাদানটিকে সরিয়ে দেয় যা উভয় সেটে উপস্থিত থাকে। নিম্নলিখিত উদাহরণ বিবেচনা করুন:
'''
#  Using ^ operator

a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 9, 8, 10}
c = a ^ b
print(c)
# Using symmetric_difference() method

a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 9, 8, 10}
c = a.symmetric_difference(b)
print(c)
# Set comparisons
#
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}
Days2 = {"Monday", "Tuesday"}
Days3 = {"Monday", "Tuesday", "Friday"}

# Days1 is the superset of Days2 hence it will print true.
print(Days1 > Days2)

# prints false since Days1 is not the subset of Days2
print(Days1 < Days2)

# prints false since Days2 and Days3 are not equivalent
print(Days2 == Days3)
# FrozenSets
Days1.issubset(Days1)

