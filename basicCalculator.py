
"""
t1soft.github.io/pythonbasicprojects


Basic Calculator
By: t1soft

Version ALPHA 0.01

"""







# Set Variable that the Calculator will use

a = 0
b = 0
c = 0
d = 0
x = "none"
solution1 = 0
runperm = "true"
cont = "yes"



# Shows Program Information

print(" ")
print(" ")
print(" ")
print(" Welcome to the Basic Python Calculator")
print(" By: t1soft")
print(" version alpha 0.01 running off python 3.9")
print(" ")


while runperm == "true":


 # Asks User for Equation

 c = input(" Enter the First Number in the Equation, Then Press Enter: ")
 print(" ")

 x = input(" Enter a Operation (+, -, *, /), Then Press Enter: ")
 print(" ")

 d = input(" Enter the Second Number in the Equation, Then Press Enter: ")
 print(" ")



 # Calculate the Solution to the Equation, then Display it

 a = int(c)
 b = int(d)

 if x == "+":
  solution1 = int(a + b)
    
 if x == "-":
  solution1 = int(a - b)

 if x == "*":
  solution1 = int(a * b)

 if x == "/":
  solution1 = int(a / b)

 print(" The Answer is:", solution1)
 print(" ")
 print(" ")


 print(" 1 = Exit")
 print(" 2 = Continue")
 print(" Type the Number Option, the Press ENTER.")

 cont = input("")

 if cont == "1":
     break

 if cont == "2":
     print(" ")
     print(" ")
 







