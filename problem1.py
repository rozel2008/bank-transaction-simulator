#Write a python program to simulate a simple bank account. The account starts with ₹5000.Bank menu should have deposit, withdraw, check balance and then exit option.
balance = 5000
while True:
    print("-" * 30, "WELCOME TO OUR BANK MENU", "-" * 30)
    print("1. Deposit")
    print("2. Withdarw")
    print("3. Check balance")
    print("4. Exit")
    print("-" * 30)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter the amount to be deposited: "))
        if amount < 0:
            print("Invalid Amount")
        else:
            balance += amount
            print(f"{amount} deposited successfully and current balance is {balance}")
    elif choice == 2:
        amount = int(input("Enter the amount to be withdrawn: "))
        if amount > balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            balance -= amount
            print(f"{amount} withdrawn successfully and current balance is {balance}")
    elif choice == 3:
        print("Current balance: ", balance)
    elif choice == 4:
        print("Thank you for using our bank system")
        break
    else:
        print("INVALID CHOICE, PLEASE TRY AGAIN")
    

