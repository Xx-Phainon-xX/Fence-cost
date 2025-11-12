#Fence cost
#Author: Joanna Liao
#Date: 29-10-2025
#Version 2.0

#Number checker
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

name=input("Welcome to my fence cost calculator, what is your name? ")

keep_going= ""
while keep_going == "":
  #Get width 
  width= (num_check(f"{name}, please enter your shape's width in metres "))
  length= (num_check(f"{name}, please enter your shapes's length in metres "))
  cost= (num_check(f"{name}, please enter the cost of the shape per metres "))

  #calculate cost
  perimeter = 2 * (width + length)
  price = perimeter * cost

  #output price
  print(f"{name}, your cost for a fence with a perimeter of {perimeter}m is ${price}")
  keep_going=(input("Please press enter if you wish to continue or any key to quit"))

