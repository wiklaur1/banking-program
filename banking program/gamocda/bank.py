#phyton banking program


def Show_balance():
    print(f"Your balance is ${balance:.2f}")

def Deposit():
    amount = float(input("enter an amount to be deposited: "))

    if amount < 0:
        print("that's not a valid amount")
        return
    else:
        return amount

def Withdraw():
    amount = float(input("enter amount to be withdraw: "))


    if amount > balance:
        print("insufficient funds")
    elif amount < 0:
        print("amount must be greater than 0")
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("bank")
    print("1.Show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        Show_balance()
    elif choice == '2':
         balance += Deposit()
    elif choice == '3':
        balance -= Withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("That is not a valid choice")

    
print("Thank you! have a nice day!")
