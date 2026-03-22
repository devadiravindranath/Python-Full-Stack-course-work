
def Zero_Division_Error_Errorcase():
    try:
        transactions = []
        average = sum(transactions) / len(transactions)
        print("Average Transaction:", average)
    except ZeroDivisionError:
        print("Error: No transactions available to calculate average.")


def Value_Error_case():
    try:
        withdrawal_amount = int("100abc")   # Invalid conversion
        print("Withdrawing:", withdrawal_amount)
    except ValueError:
        print("Error: Invalid value entered. Please enter a numeric amount.")


def Type_Error_case():
    try:
        balance = 500
        deposit_amount = "100"   # String instead of int
        new_balance = balance + deposit_amount
        print("New Balance:", new_balance)
    except TypeError:
        print("Error: Cannot add string to integer. Please enter numeric value.")


def Index_Error_case():
    try:
        transactions = [100, 200, 300]
        print("Transaction:", transactions[5])
    except IndexError:
        print("Error: Transaction index out of range.")


def Key_Error_case():
    try:
        accounts = {"101": "Savings", "102": "Current"}
        print("Account Type:", accounts["105"])
    except KeyError:
        print("Error: Account does not exist.")


def file_not_found_error_case():
    try:
        with open("transaction_log.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Error: Transaction log file not found.")
# -------- MAIN MENU --------
while True:
    print("\n--- ATM SIMULATION MENU ---")
    print("1. Check Average Transaction (ZeroDivisionError)")
    print("2. Withdraw with Invalid Input (ValueError)")
    print("3. Deposit with Invalid Data Type (TypeError)")
    print("4. Access Invalid Transaction History (IndexError)")
    print("5. Access Non-Existent Account (KeyError)")
    print("6. Read Missing Transaction Log File (FileNotFoundError)")
    print("7. Exit")

    choice = input("Select an option (1-7): ")

    if choice == "1":
        Zero_Division_Error_Errorcase()
    elif choice == "2":
        Value_Error_case()
    elif choice == "3":
        Type_Error_case()
    elif choice == "4":
        Index_Error_case()
    elif choice == "5":
        Key_Error_case()
    elif choice == "6":
        file_not_found_error_case()
    elif choice == "7":
        print("Thank you! Exiting ATM Simulation.")
        break
    else:
        print("Invalid choice! Please select between 1 and 7.")


