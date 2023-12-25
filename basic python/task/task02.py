def convertToTuple(itr):
    return tuple(itr)


def convertToList(itr):
    return list(itr)


x = 20
getTuple = convertToTuple(range(x))
getList = convertToList(getTuple)
# getList.append('some text')
# getTuple = convertToTuple(getList)
# print(getTuple)
getList.extend(['age'])

x = [
    {
        "name": "X",
        "account_number": 123,
        "pass": 1234,
        "balance": 0,
    },
    {
        "name": "Y",
        "pass": 1111,
        "account_number": 124,
        "balance": 0,
    },
    {
        "name": "Z",
        "account_number": 125,
        "pass": 1122345345,
        "balance": 0,
    }
]

print('''
      1. Send Money \n
      2. Payment \n 
      3. Cash out \n
      4. Add money \n
      5. My Bkash
      ''')
option = int(input('your choice'))
