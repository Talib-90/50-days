# def format_name(fname, lname):
#     return str(fname + lname).title()

# output = format_name("talib ", "ilahi")

# def format_name(fname, lname):
#     """Take a first and last name and 
#     format it to return a title case version of the name"""
#     if fname == "" or lname == "":
#         return "you did not provide valid inputs."
#     format_fname = fname.title()
#     format_lname = lname.title()

#     return f"result {format_fname} {format_lname}."

# print(format_name(input("What is your fname? "), input("What is your lname? ")))


# Calculator
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# print(operation["*"](4,8))


def calculator():
    should_continue = True
    num1 = float(input("Enter first number: "))

    while should_continue:
        for symbol in operation:
            print(symbol)
        choose_symbol = input("Pick an operation: ")
        num2 = float(input("Enter second number: "))
        answer = operation[choose_symbol](num1, num2)
        print(f"{num1} {choose_symbol} {num2} = {answer}")

        choose = input(f"Type 'y' for continue calculating with {answer}. Type n to stop.").lower()

        if choose == 'y':
            num1 = answer
        else:
            should_continue = False
            # print("\n" * 20)
            # calculator()


calculator()