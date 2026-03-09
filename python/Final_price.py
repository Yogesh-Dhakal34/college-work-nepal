# WAP to find final price after discount.

Item_1 = float(input("Enter the price of item 1: "))
Item_2 = float(input("Enter the price of item 2: "))
Item_3 = float(input("Enter the price of item 3: "))


Total_price = Item_1 + Item_2 + Item_3
Discount = Total_price * 0.10
Final_price = Total_price - Discount


print(f"The Total price before discount is: {Total_price:.2f}")
print(f"The discounted amount is: {Discount:.2f}")
print(f"The Final price after discount is: {Final_price:.2f}")
