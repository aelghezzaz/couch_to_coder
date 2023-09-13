ilename = "control_flow_atm.py"
balance = 1000
pin = 9742

user_pin = int(input("Enter your PIN: "))
if user_pin == pin:
    print(f"Your balance: ${balance}")
    choice = input("Withdraw or deposit? (w/d): ")
    if choice == "w":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrawal successful. New balance: ${balance}")
        else:
            print("Insufficient balance.")
    elif choice == "d":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit successful. New balance: ${balance}")
else:
    print("Invalid PIN.")