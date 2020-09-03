'''Calculator function created by Harsh Soni'''
# Welocme Message
print("Howdy User!","Welcome to the Calculator Program created by programmer Harsh Soni.")
print("Have a great Experience ahead!")
# Calculator Class Defined by the name Calculator()
class calculator():



    print ( "                    GLOSSARY\n"
            "    Use:\n"
            "      + for Addition\n"
            "      - for Subtraction\n"
            "      * for Multiplication\n"
            "      / for Division\n"
            "      ^ for Exponant\n"
            "      ** for Exponant\n"
            "      % for Modulus\n"
            "    " )



def operation():
    sym = input( "Please select any one from the above symbols for the calculation: " )

    num1 = int (input("Number 1: ") )
    num2 = int (input("Number 2: ") )
    if sym == "+":
        print ( "Answer:  ", num1 + num2 )
        ret_msg ()
    elif sym == "-":
        print ( "Answer:  ", num1 - num2 )
        ret_msg ()
    elif sym == "*":
        print ( "Answer:  ", num1 * num2 )
        ret_msg ()
    elif sym == "/":
        print ( "Answer:  ", num1 / num2 )
        ret_msg ()
    elif sym == "^":
        print ( "Answer:  ", num1 ** num2 )
        ret_msg ()
    elif sym == "%":
        print ( "Answer:  ", num1 % num2 )
        ret_msg ()
    elif sym == "**":
        print ( "Answer:  ", num1 ** num2 )
        ret_msg ()
    else:
        print ( "Invalid Operator" )
        print("[",sym,"]""Operator not defined!")
        # do u like to continue. Y for return AND N for quit



import time
def ret_msg():
    print("")
    time.sleep(1)
    msg = int ( input ( "Press 0(Zero) to end & 1(One) to continue: " ) )
    if msg == 1:
        print ( "" )
        return operation ()
    elif msg == 0:
        print ( "" )
        print ( "Thanks for using this Calculator!" )
        print("A Calculator Program by: HARSH SONI")
    elif msg != (1,0):
        print ( "Invalid Input" )
        print ( "Program Terminated" )
    else:
        print("Invalid Input")
        print("Program Terminated")
        return






operation()
calculator()
