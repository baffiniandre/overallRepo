import math
def sqrtOperator():
    number1 = int(input("Insert an argument for the square root: "))
    try:
        result = math.sqrt(number1)
    except ValueError:
        print("number provided of the correct type")
    except:
        print("Number is not correct")
    else:
        print("Result: ", result)

def complex_calculation(num):
    try:
        result = num / (num - 5)
        print (f"Result: {result}")
    except Exception as e:
        print("An error occurred during calculation: ", e)

#test sqrtOperator:
print("Testing sqrtOperator function")
sqrtOperator()

#test complex_calculation:
print("Testing complex_calculation function")
user_input = float(input("Enter a number: "))
complex_calculation(user_input)

