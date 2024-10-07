#showing the initial balance of the user 
def show_balance():
    print(f"your balance is shs{balance:.3f}")
#incaes the user wants to deposit . this adds the deposited income to the balance
def deposit():
    amount=float(input("Enter an amount to be deposited: "))
    if amount<0:
        print("sorry you cant deposit that")
        return 0
    else:
         print("Thank you for depositing");
         return amount

def withdraw():
    amount =float(input("enter the amount you want to withdraw  "))
    if amount >balance:
        print("insufficient balance ")
        return 0
    elif amount>0:
        print("amount should be greater than zero ")
        return 0
    else:
        return amount
    
    
balance = 0
is_running = True
while is_running:
    print("\n The banking program")
    print("1.show balance")
    print("2. deposit")
    print("3.withdraw")
    print("4.exit")
    
    choice = input("enter your choice (1 to 4)  " )
    if choice =="1":
     show_balance()
    elif choice =="2":
      balance += deposit()
    elif choice =="3":
      balance-=withdraw()
    
    elif choice=="4":
       is_running = False
    else:
       print("Thats  invalid")
print("Thank you and have a nice day ")
print ("This system was developed by Cyrus")

