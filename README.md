# Python-Exercise-4-1
Lab 4 - Future Value Calculator



``` python


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


# Jeff Bohn
# SWDV-210 Lab 4 : Future Value Calculator
# 8/30/2024
# validation.py 


# Learning docstrings in Python
# 1 - Does it give a high level overview of what you are trying to accomplish?
# 2 - Does it have full coverage of arguments passed in?
# 3 - Does it cover the method or class return type and return value?
# 4 - Understand how my team operates/communicates and note accordingly
# 5 - Type hinting can be useful in loose languages like Python



def getFloat(prompt, low, high):
    
    """
    getFloat() validates user input for the specific number range \n
    args: float(prompt), int(low), int(high) \n
    return: float(userNumber)
    """
    # run indefinitely (keep asking user) until return statement
    while True:
        userNumber = float(input(prompt))
        if (low <= userNumber and userNumber <= high):
            return userNumber
        else:
            print(f"Enter a number greater than {low} and less than or equal to {high}")


def getInt(prompt, low, high):
    
    """
    getInt() validates user input for the specific number range \n
    args: int(prompt), int(low), int(high) \n
    return: int(userNumber)
    """
    
    while True:
        userNumber = int(input(prompt))
        if (low <= userNumber and userNumber <= high):
            return userNumber
        else:
            print(f"Enter a number greater than {low} and less than or equal to {high}")
```
