#Making A Simple Calculator with Python Firtst,Let's write the code for User input

#Addition Function
def Addition(a,x):
    sum =  a + x
    return sum
#Subtraction Function
def Subtraction(s,t):
    minus = s-t
    return minus

#Multiplication Function
def Multiplication(c,d):
    multiply = c*d
    return multiply

#Dividion Function
def Division(e,f):
    divide = e/f
    return divide

#Exponent Function
def Exponent(v,m):
    Exp =  v**m
    return Exp

#Change a number to Binary Function
def decimalToBinary(n): 
    return bin(n).replace("0b", "")

#Taking User's Input for the name, multiple print statements
user_name = input("Please Write your Name")
print("Welcome", (user_name),",Hope you are having a Good Day!")
print("Write the following number from the list to perform Opreation")
print("1.Addition")
print("2.Subtraction")
print("1.Multiplication")
print("1.Dividion")
print("1.Exponent")
print("1.Change to Binary Note: Only 1st number will be coonverted to Binary. Just write Anything in 2nd Number")
#Taking User Input for the following number to perform Opreation
user1 = int(input("Write the Number"))
# Taking User's input for the numbers
numb1 = int(input("Write your First Number"))
numb2 = int(input("Write your Second Number"))

#Witing Conditions
if user1 == 1:
    print(Addition(numb1,numb2))
elif user1 == 2:
    print(Subtraction(numb1,numb2))
elif user1 == 3:
    print(Multiplication(numb1,numb2))
elif user1 == 4:
    print(Division(numb1,numb2))
elif user1 == 5:
    print(Exponent(numb1,numb2))
elif user1 == 6:
    print(decimalToBinary(numb1))
else:
    print("Error: Please try Again ")
