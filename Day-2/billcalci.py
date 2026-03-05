name = input("Enter the name: ")
mobile_no = int(input("Enter the Mobile number: "))

product_1 = input("Enter the product name: ")
price_1 = float(input("Enter the product_1 price: "))

product_2 = input("Enter the product name: ")
price_2 = float(input("Enter the product_2 price: "))

product_3 = input("Enter the product name: ")
price_3 = float(input("Enter the product_3 price: "))

print(f"\n{name}, your bill details:")
print(f"{product_1}: ₹{price_1}")
print(f"{product_2}: ₹{price_2}")
print(f"{product_3}: ₹{price_3}")

total_bill = price_1 + price_2 + price_3
print(f"Total Bill Amount: ₹{total_bill}")
