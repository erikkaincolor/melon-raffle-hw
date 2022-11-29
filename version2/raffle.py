
from random import choice
from customers import get_customers_from_file

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():           #makes it run!
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)

if __name__=="__main__": #i added this to make it run 
    run_raffle()            #i added this to make it run 