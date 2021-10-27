# Mini Assessment (10 marks)
#
# Consider the following description:
#
# We wish to create a program that helps Peter Pan (a boy with an interesting lifestyle) and his friends fly.
# The program consists of three functions:
#
# Function: happy_thought
#
# Requirements:
# [1] The function should be named happy_thought and should have no parameters.
# [2] The function should then display the message "What is your happy thought?"
# [3] The function should then read in the user's response.
# [4] The function should then display the message "Think about {thought}." where {thought} is the user's response.
# [5] Finally, the function should display the message "It will help you fly!".
# A template of this function is given below. Note that requirement 1 above has already been completed for you.
#
# def happy_thought():
#   # TO DO: display initial message here (requirement 2 above)
#   # TO DO: read and store user's response here (requirement 3 above)
#   # TO DO: display the thought message here (requirement 4 above)
#   # TO DO: display the final message here (requirement 5 above)
#
# A suitable call to the function is given below. This can be used to execute the function.
#
# happy_thought()
#
# The output from a sample run of the function is shown below.  This can be used to check the execution of your function.
# What is your happy thought?
# Neverland
# Think about Neverland.
# It will help you fly!
#
# The assessment criteria for this function are shown below.  You should use this to check that you have met all the criteria for this function:
#
# Marks for this function are allocated as follows:
#
# 1 mark: correctly displays initial messages
# 1 mark: correctly reads user's response
# 1 mark: correctly displays the final message with the user's response
# Function: pixie_dust
#
# Requirements:
# [1] The function should be named pixie_dust.
# [2] The function should have 1 parameter named amount which represents the amount of pixie dust that has been used.
# [3] The function should start by checking if the amount is greater than 0.
# [4]     The function should display the message "The pixie dust will help you fly!" if the amount is greater than 0.
# [5]     Otherwise, the function should display the message "You will need a bit of pixie dust to fly!".
#
# Some suitable calls to the function are given below. This can be used to execute the function.
#
# pixie_dust(0) # Should display "You will need a bit of pixie dust to fly!"
# pixie_dust(3) # Should display "The pixie dust will help you fly!"
#
# The output from a sample run of the function with the above function calls is shown below.  This can be used to check the execution of your function.
# You will need a bit of pixie dust to fly!
# The pixie dust will help you fly!
#
# The assessment criteria for this function are shown below.  You should use this to check that you have met all the criteria for this function:
#
# Marks for this function are allocated as follows:
#
# 1 mark: the function signature is correct
# 1 mark: an appropriate if...else statement has been used
# 1 mark: the correct output is displayed
# Function: fly
#
# Requirements:
# [1] The function should be named fly.
# [2] The function should have 1 parameter named people which represents the number of people that will fly with Peter Pan.
# [3] For each person in people, the following should be done:
# [4]    Display the message "Sprinkling some pixie dust..."
# [5] Finally, the function should display "It is time to fly to Neverland!".
#
# A suitable call to the function is given below. This can be used to execute the function.
#
# fly(3)
#
# The output from a sample run of the function with the above function calls is shown below.  This can be used to check the execution of your function.
# Sprinkling some pixie dust...
# Sprinkling some pixie dust...
# Sprinkling some pixie dust...
# It is time to fly to Neverland!
#
# The assessment criteria for this function are shown below.  You should use this to check that you have met all the criteria for this function:
#
# Marks for this function are allocated as follows:
#
# 1 mark: the function signature is correct
# 1 mark: a loop has been implemented
# 1 mark: the loop executes correctly
# 1 mark: the correct output is displayed
def happy_tonight():
    print("What is your happy thought?")
    thought = input()
    print(f"Think about {thought}.")
    print("It will help you fly!")

happy_tonight()


def pixie_dust(amount):
   if amount > 0:
       print("The pixie dust will help you fly!")
   else:
       print("You will need a bit of pixie dust to fly!")
pixie_dust(0)
pixie_dust(4)

def fly(people):
    for x in range(0, people, 1):
        print("Sprinkling some pixie dust...")
    print("It is time to fly to Neverland!")
fly(3)
# def happy_tonight():
#     print("What is your happy thought?")
#     thought = str(input(""))
#     print(f"Think about {thought}.")
#     print("It will help you fly!")
#
# # happy_tonight()
#
# def pixie_dust(amount):
#     if amount > 0:
#         print("The pixie dust will help you fly!")
#     else:
#         print("You will need a bit of pixie dust to fly!")
#
# # pixie_dust(0)
# # pixie_dust(3)
#
# def fly(people):
#     for person in people:
#         print("Sprinkling some pixie dust...")
#     print("It is time to fly to Neverland!")
#
# fly(3)
