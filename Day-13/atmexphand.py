while True:
    print("\n---ATM SIMULATION MENU---")
    print("1.Check Average Transaction(ZeroDivisionError)")
    print("2.Withdraw with Invalid Input(ValueError)")
    print("3.Deposit with Invalid Data Type (Type Error)")
    print("4.Access Invalid Transaction History ")
    print("5.Access Non-Existent Account (KeyError)")
    print("6.Read Missing Transaction Log File (FileNotFoundError) ")
    print("7.Exit ")

    choice=input("select an option(1-7):")

    if choice =="1":
        Zero_Division_Error_Errorcase()
    elif choice=="2":
        Value_Error_case()
    elif choice=="3":
        Type_Error_case()
    elif choice=="4":
        Index_Error_case()
    elif choice=="5":
        Key_Error_case()
    elif choice=="6":
        file_not_found_error_case()
    elif choice == "7":
        print("EXIT")


def Zero_Division_Error_Errorcase():
    try:

def Value_Error_case():
    try:
        withdrawl_amount=int("100/0")
        print("withdrawing:",withdrawl_amount)
    except valuerror:
        print("error:Invalid value entered. Please enter a numeric amount.")

def Type_Error_case():
    try:
        balance=500
        deposit_amount="100"
        new_balance=balance+deposit_amount
        
        
        
        
    
    
