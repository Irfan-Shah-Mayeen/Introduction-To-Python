#exception = events detected during execution that interrupt the flow of a program
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int (input("Enter a numbr  to divide by:"))
    result = numerator / denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("you can't divided by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only number plz")
except Exception as e:
    print(e)
    print("Something went wronng:")
else:
    print(result)
finally:
    print("this is alyaws execute")