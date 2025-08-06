# A programme that take input of redius of a circle and print its circumference and area useing math.pi 
import math 
redius = float(input("Enter Redius - "))

circumference = 2 * math.pi * redius
Area = math.pi * redius**2

print("circumference : ",circumference)
print("Area : ", Area)
