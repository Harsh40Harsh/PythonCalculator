"""Calculator function created by hash_f(x)"""

# Welcome Message
import time

print("Howdy User!", "Welcome to the Calculator Program created by programmer Harsh Soni.")
print("Have a great Experience ahead!")


# Calculator Function Defined by the name Calculator()
def calculator():
    print("                    GLOSSARY\n"
          "    Use:\n"
          "      + for Addition\n"
          "      - for Subtraction\n"
          "      * for Multiplication\n"
          "      / for Division\n"
          "      ^ for Exponent\n"
          "      ** for Exponent\n"
          "      % for Modulus\n"
          "      ! for Factorial\n"
          "      p for Prime Number\n"
          "      hcf for HCF\n"
          "    ")


# All Functions here...
# Return Message
def ret_msg():
    print("")
    time.sleep(0.8)
    msg = (input("Press 0(Zero) to end & 1(One) to continue: "))  # int
    if msg == "1":
        print("")
        return operation()
    elif msg == "0":
        print("")
        print("Thanks for using this Calculator!")
        print("A Calculator Program by: HARSH SONI")
    else:
        print("Invalid Input")
        print("Program Terminated")


def primenumber():
    n = int(input("Number to be Checked: "))
    if n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                print(f"{n} is not a prime number")
                print(f"{i} times {n // i} is {n}")
                break
            else:
                print(n," is a Prime Number.")
                break
    else:
        print("Invalid Input")


def hcfofnumber(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
            return hcf


def operation():
    sym = input("Please select any one from the above symbols for the calculation: ")
    if sym == "+":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()
        print("Answer:  ", num1 + num2)
        ret_msg()
    elif sym == "-":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()

        print("Answer:  ", num1 - num2)
        ret_msg()
    elif sym == "*":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()

        print("Answer:  ", num1 * num2)
        ret_msg()
    elif sym == "/":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()

        print("Answer:  ", num1 / num2)
        ret_msg()
    elif sym == "^":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()

        print("Answer:  ", num1 ** num2)
        ret_msg()
    elif sym == "%":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()

        print("Answer:  ", num1 % num2)
        ret_msg()
    elif sym == "**":
        try:
            num1 = int(input("Number 1: "))
            num2 = int(input("Number 2: "))
        except:
            print("              False Input Observed")
            time.sleep(0.5)
            print("              Restarting Programme!")
            return operation()

        print("Answer:  ", num1 ** num2)
        ret_msg()
    elif sym == "p" or "P":
        return primenumber()
    elif sym == "hcf":
        try:
            x = int(input("X: "))
            y = int(input("Y: "))
            print(f"HCF of {x} and {y} is {hcfofnumber(x, y)}")
        except:
            print("Invalid Input")
    else:

        print("Invalid Operator")
        print("[", sym, "]""Operator not defined!")
        # would u like to continue. Y for return AND Q for quit
        ret = input("Press Y to Continue and Q to Quit: ")
        print("+")
        if ret == "Y":
            return operation()
        elif ret == "y":
            return operation()
        elif ret == "Q":
            return quit()
        elif ret == "q":
            return quit()
        else:
            print("Pseudo Input Observed...")
            time.sleep(0.2)
            print("Terminating Program...")
            return quit(0)
    pass


# Functions Defined Above, Called for Execution Below!

calculator()
operation()

# HCF Computation
# x = int(input("X: "))
# y = int(input("Y: "))


# def hcfofnumber(x,y):
#
#     if x>y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if ((x%i == 0) and (y%i == 0)):
#             hcf = i
#             return hcf
