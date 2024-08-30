# Jeff Bohn
# SWDV-210 Lab 4 : Future Value Calculator
# 8/30/2024
# main.py


import validation as isValid

def calculate_future_userNumber(monthly_investment, yearly_interest_rate, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value


def main():
    choice = "y"
    while choice.lower() == "y":

        monthly_investment = isValid.getFloat("\nEnter monthly investment:\t", low=0, high=1000)

        yearly_interest_rate = isValid.getFloat("\nEnter yearly interest rate:\t", low=0, high=15)

        years = isValid.getInt("\nEnter number of years:\t\t", low=0, high=50)

        # get and display future userNumber
        future_userNumber = calculate_future_userNumber(monthly_investment, yearly_interest_rate, years)

        print(f"Future value:\t\t\t ${round(future_userNumber, 2)} ")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
