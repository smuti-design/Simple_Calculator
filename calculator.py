import pandas as pd
import numpy as np
import os

class Math:
    def __init__(self,num1,num2,operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator
    def addition(self,a,b):
        add = a+b
        return add
    def substraction(self,a,b):
        subtract = a-b
        return subtract
    def multipy(self,a,b):
        multipy = a * b
        return multipy
    def division(self,a,b):
        divide = a/b
        return divide

num1_inp= int(input("Please enter a number.\n"))
num2_inp= int(input("Please enter another number.\n"))
usr_operator = input("Enter an operator.\n")

calc = Math(num1_inp,num2_inp,usr_operator)

if usr_operator == "+":
    print(calc.addition(calc.num1,calc.num2))
elif usr_operator == "-":
    print(calc.substraction(calc.num1,calc.num2))
elif usr_operator =="*":
    print(calc.multipy(calc.num1,calc.num2))
elif usr_operator == "/":
    print(calc.division(calc.num1,calc.num2))

else:
    print("invalid operator")

