#Calculator app - I did it a new minimal way 
def calculator(fnum):
    print("+\n-\n*\n/")
    operation = input("Choose the operation ")
    sec_num = int(input("Whats the second number? "))

    output = 0

    if operation == "+":
        output = fnum + sec_num
    elif operation == "-":
        output = fnum - sec_num
    elif operation == "*":
        output = fnum * sec_num
    elif operation == "/":
        output = fnum / sec_num

    answer = float(output)
    print(f"The result is {answer}")


    calc_continue = input(f"Type 'y' if you wish to keep calculating "
    "with {answer}, or type 'n' to start a new calculation: ")

    if calc_continue == "y":
        calculator(answer)
    else:
        calculator(int(input("Whats the first number? ")))

calculator(int(input("Whats the first number? ")))
