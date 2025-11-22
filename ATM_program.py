balance = 0

while True:
    print("\n--- ATM Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = input("Choose an option: ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful.")

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    elif choice == '3':
        print(f"Current Balance: {balance}")

    elif choice == '4':
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice, try again.")
