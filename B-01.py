#Fence cost
#Author: Joanna Liao
#Date: 29-10-2025
#Version 2.0

#Number checker that checks whether the value inserted is more than 0
#If the number is less than 0, it would print error
def num_check(question):
    error= f"Please eneter a value that is more the 0 \n"
    while True:
       try:
            response=float(input(question))
            if response>0:
               break
            else:
                print(error)
       except: ValueError
       (print(error))
    return response

#Welcome code to make it more human
name=input("Welcome to my fence cost calculator, what is your name? ")

#loop code so the program can go on and on if the user desires
#If they don't want to continue they press any other key to quit
keep_going= ""
while keep_going == "":
  #These variables get the value of the width, length, and cost
  width= (num_check(f"{name}, please enter your shape's width in metres "))
  length= (num_check(f"{name}, please enter your shapes's length in metres "))
  cost= (num_check(f"{name}, please enter the cost of the shape per metres "))

  #calculates the cost of the fence 
  perimeter = 2 * (width + length)
  price = perimeter * cost

  #outputs the price for the user to see
  print(f"{name}, your cost for a fence with a perimeter of {perimeter}m is ${price}")
  keep_going=(input("Please press enter if you wish to continue or any key to quit"))

  

