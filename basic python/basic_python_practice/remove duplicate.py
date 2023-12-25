inp1 = input()
try:
 inp = [int(inp1)]
 list = [17, 9, 8, 5, 6]
 for x in inp:
    if x in list:
        print("already have")
        continue
    else:
        list.append(int(inp1))
except:
    print("only integer")
print(list)