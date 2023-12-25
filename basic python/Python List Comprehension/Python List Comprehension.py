x = list(range(0, 100))
# newlist = [expression for item in iterable if condition == True]
num = [pow(n,3) for n in x if n % 2 == 0]
print(num)

number_list = [ num for num in range(30) if num % 2 != 0]  
print(number_list)  