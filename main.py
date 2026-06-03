import addition
import subtraction
import multiplication
import division
import power
import modulus
import floor_division

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", addition.add(a,b))
print("Subtraction =", subtraction.subtract(a,b))
print("Multiplication =", multiplication.multiply(a,b))
print("Division =", division.divide(a,b))
print("Power =", power.power(a,b))
print("Modulus =", modulus.modulus(a,b))
print("Floor Division =", floor_division.floor_division(a,b))