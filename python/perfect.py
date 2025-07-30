# A Python program to check if a number is perfect
number = int(input("Enter Number - "))

sum_of_factors = 0

for i in range(1, number):
    if number % i == 0:
        sum_of_factors += i

if sum_of_factors == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")