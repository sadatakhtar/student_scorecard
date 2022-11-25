"""
A restaurant ordering program
"""
menu = {'cheese burger': 1.50, 'chicken burger': 2.50, 'mixed grill': 15.50, 'pasta': 3.50, 'samosa': 2}
customers_order_total = []


def greeting():
    # A welcome function
    print('*' * 35)
    print('*' * 4 + ' Welcome to the restaurant ' + '*' * 4)
    print('*'* 35)

def user_input():
    # Takes user input of how many customers are eating in
    number_of_customers = int(input("How many people are dining today? "))
    return number_of_customers


def reserve_table(number_of_customers):
    # Creates number of customers per table list
    total_range = range(1, number_of_customers +1)
    table = list(total_range)
    return table


def take_individual_order():
    # Asks all customers their order and adds to a list to calculate total
    option = 'x'
    sum_of_order = 0

    while not option == 'N':
        ordered_so_far = float(input("What would you like to order? "))
        sum_of_order += ordered_so_far
        option = input("Do you want to continue your order? [Y/N]").upper()
    customers_order_total.append(sum_of_order)
    print("Customers order taken and added to total")
    return sum_of_order


def start_table_order():
    greeting()
    customer_head_count = user_input()
    size_of_table = reserve_table(customer_head_count)

    customer_total = 0
    for customer in size_of_table:
        total = take_individual_order()
        customer_total += total
    return customer_total

# TODO: Calculate overall total and grade with message






