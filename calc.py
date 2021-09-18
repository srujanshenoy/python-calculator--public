# python calculator
# we are going to define the functions (add subtract multiply and divide)
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x/y


def exponentiation(x, y):
    return x ** y


def help():
    print("Select an operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.exponentiation")
    print("0.exit")


help()
while True:
    #
    choice = input("Enter choice(0/1/2/3/4/5):")

    if choice == '1':
        opp_choice = "Add"
    elif choice == '2':
        opp_choice = "Subtract"
    elif choice == '3':
        opp_choice = "Multiply"
    elif choice == '4':
        opp_choice = "Divide"
    elif choice == "5":
        opp_choice = "exponentiation"
    elif choice == '0':
        opp_choice = "please exit"
    else:
        opp_choice = "undifined"

    print("Your choice is", opp_choice)

    if choice in ('1', '2', '3', '4', '5', '0'):
        # if u want to break you enter '0'
        if choice == '0':
            print("Bye Bye!")
            break
        x = float(input("Enter the first number:"))
        y = float(input("Enter the second number:"))
# we had given options of what you can enter, they enter the number of the operation.
# then we use the function we Defined earlier and print the result of what they enter
# for the values.
        if choice == '1':
            print(x, "+", y, "=", add(x, y))
        if choice == '2':
            print(x, "-", y, "=", subtract(x, y))
        if choice == '3':
            print(x, "x", y, "=", multiply(x, y))
        if choice == '4':
            print(x, "/", y, "=", divide(x, y))
        if choice == '5':
            print(x, '^', y, exponentiation(x, y))
    else:
        print("Invalid Choice, try again")
        help()
    help()
