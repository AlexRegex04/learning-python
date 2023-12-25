
user_info_db = [
    {
        "name": "X",
        "account_number": 123,
        "pass": "1234",
        "balance": 0,
    },
    {
        "name": "Y",
        "pass": "1111",
        "account_number": 124,
        "balance": 0,
    },
    {
        "name": "Z",
        "account_number": 125,
        "pass": "1122345345",
        "balance": 0,
    }
]


class ChoiceExecute(object):
    global user_info_db

    def __init__(self, u_info, full_user_info_db):
        self.u_info = u_info
        self.full_user_info_db = full_user_info_db

    def sendMoney():
        pass

    def Payment():
        pass

    def CashOut():
        pass

    def AddMoney(self):
        new_add_money = float(input("How much add money? "))

        def Add(info):
            if (info["account_number"] == self.u_info['account_number']):
                info['balance'] = self.u_info['balance'] + new_add_money
                self.u_info['balance'] += new_add_money
            return info

        update_user_info = map(Add, self.full_user_info_db)

        user_info_db = list(update_user_info)
        choice(self.u_info)


def choice(user_info):
    print(
        f'Name: {user_info["name"]}\nAccount Number: {user_info["account_number"]} \nBalance: {user_info["balance"]}')
    print('''
      1. Send Money \n
      2. Payment \n 
      3. Cash out \n
      4. Add money \n
      5. My Bkash \n 
      6. Log out
      ''')
    choice_option = int(input("Enter your choice:  "))
    execute = ChoiceExecute(user_info, user_info_db)
    match (choice_option):
        case 1:
            execute.sendMoney()
        case 2:
            execute.Payment()
        case 3:
            execute.CashOut()
        case 4:
            execute.AddMoney()
        case 5:
            # execute.sendMoney()
            pass
        case 6:
            running = False
            pass


def userInput():
    global account_number
    try:
        account_number = int(input('your account number:  '))
    except:
        print("Pleas enter valid info only you can integer input")
        account_number = int(input('your account number:  '))

    account_pass = input('Enter your password:  ')

    def checkUser(u_info): return (
        u_info['account_number'] == account_number and u_info["pass"] == account_pass)

    try:
        get_userInfo = list(filter(checkUser, user_info_db))[0]
        return get_userInfo
    except:
        return {}


running = True

x = userInput()

if (bool(len(x))):
    pass
else:
    confirm = str(
        input("Apni ki new account make korte chan: \n type yes or no:  "))
    if (confirm == 'yes'):
        name = str(input("Enter your name:  "))
        account_number = int(str(10) + str(len(user_info_db)))
        account_pass = str(input("Enter password"))
        u_info = {
            "name": name,
            "account_number": account_number,
            "pass": account_pass,
            "balance": 0
        }
        user_info_db.append(u_info)

        choice(u_info)
    else:
        running = False

# while running:
