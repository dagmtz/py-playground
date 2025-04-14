# /usr/bin/python

# User is expected to enter a positive integer, then, this script should
# calculate (not using modulo operator or direct division) whether the entered
# number is divisible by 7.
#
# There is a simple rule to implement this, for a given three digit number, 
# let's say "abc", we take the last digit out, (so we're left with "ab"), then
# double "c" and subtract it from "ab", if the resulting number is a multiple
# of 7, then, the original number ("abc") is also divisible by 7.

def is_divisible_by_7(number):
    if number < 70:
        if (number % 7) == 0:
            print("It is divisible by 7! :)")
        else:
            print("It is not divisible by 7! :(")
    else:
        op1 = str(number)
        nlength = len(op1)-1
        op2 = int(op1[:nlength])
        op1 = int(op1[nlength])
        op3 = op2 - 2*op1
        print(f"{op2}-{op1}={op3}")
        is_divisible_by_7(op1)

num = input("Enter a positive integer!: ")
num = int(num)
is_divisible_by_7(num)
            


        

