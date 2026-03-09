"""
PROJECT: Pizza Shop Point of Sale (POS) System
OBJECTIVE: Automate order processing and discount logic for a local business.

PROBLEM STATEMENT: 
The user needs to calculate the total cost for two types of pizzas: 
Regular ($10.00) and Large ($18.00). The system must:
1. Allow the user to select the pizza type and quantity.
2. Apply a 10% discount (0.9 multiplier) for take-away orders.
3. Use a continuous loop to handle multiple customers.
4. Track and display the total sales and total items sold at the end.

SKILLS DEMONSTRATED: While loops, conditional logic (if-elif-else), 
type casting, and mathematical operations.
"""
def main():
    total_sales = 0.0
    eat_in_count = 0
    take_away_count = 0

    while True:

        Pizza_type = input("Enter pizza type (R, or L), Q to quit :").upper()

        if (Pizza_type == 'Q'):
            break

        quantity = int(input("Enter quantity: "))
        service_type = input("<E>at-in or <T>ake-away? ").upper()
        

        if Pizza_type == 'R':
            price = 10.00
        elif Pizza_type == 'L':
            price = 18.00

        cost = price * quantity
        if service_type == 'T':
            cost = cost * 0.9  # Apply 10% discount
            take_away_count += 1
        else:
            eat_in_count += 1

        total_sales += cost
        print(f"The cost is ${cost:.2f}")


    print(f"Total sales = {total_sales}")
    print(f"Number of eat-in = {eat_in_count}")
    print(f"Number of take-away = {take_away_count}")
main()
