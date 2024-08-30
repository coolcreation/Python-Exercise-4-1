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
