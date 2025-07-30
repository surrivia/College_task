# A Python program that asks the user for one number and tells if it is a prime number or not
#used for loop if else
number = int(input("Enter Number - "))

if number == 1:
    print(number, "is not a Prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not a Prime number")
            break
    else:
        print(number, "is a Prime number")