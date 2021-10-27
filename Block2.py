# Mini Assessment (10 marks)
#
# Consider the following description:
#
# We wish to create a program to learn about Scooby Doo (a Great Dane dog) and his friends (a gang of teenagers).
# The program consists of three functions:
#
# Function: gang
#
# Requirements:
# [1] The function should be named gang and should have no parameters.
# [2] The function should start by displaying the message "Loading gang...".
# [3] The function should then create a list named friends.
# [4] The function should then populate the list with the following values:
# "Scooby Doo"
# "Shaggy Rogers"
# "Fred Jones"
# "Daphne Blake"
# "Velma Dinkley"
# [5] The function should then display the list.
# [6] The function should then display the message "...Done!".
# [7] Finally, the function should return the list.
#
#
# A suitable call to the function is given below. This can be used to execute the function.
#
# gang()
#
# The output from a sample run of the function is shown below.  This can be used to check the execution of your function.
# Loading gang...
# ['Scooby Doo', 'Shaggy Rogers', 'Fred Jones', 'Daphne Blake', 'Velma Dinkley']
# ...Done!
#
# Function: phrases
#
# Requirements:
# [1] The function should be named phrases.
# [2] The function should have 1 parameter named friends which represents a list of friends.
# [3] The function should start by creating a dictionary named quotes.
# [4] For each friend in the list of friends, the function should do the following:
# [5]     Display the message "What does {friend} say?" where {friend} is the name of the friend.
# [6]     Read in the user's response and store it in a variable named quote.
# [7]     Add the value assigned to quote to the dictionary quotes using the friend's name as a key.
# [8] Finally, the function should return the dictionary quotes.


# A suitable call to the function is given below. This can be used to execute the function.
#
# friends = gang()
# quotes = phrases(friends)
# print(f"\nPhrases: {quotes}\n")
#
# The output from a sample run of the function with the above function call is shown below.  This can be used to check the execution of your function.
# What does Scooby Doo say?
# Scooby Dooby Doo!
# What does Shaggy Rogers say?
# Zoinks!
# What does Fred Jones say?
# Hold the phone!
# What does Daphne Blake say?
# Jeepers!
# What does Velma Dinkley say?
# Jinkies!
#
# Phrases: {'Scooby Doo': 'Scooby Dooby Doo!', 'Shaggy Rogers': 'Zoinks!', 'Fred Jones':'Hold the phone!', 'Daphne Blake': 'Jeepers!', 'Velma Dinkley':'Jinkies!'}
#
#
# The assessment criteria for this function are shown below.  You should use this to check that you have met all the criteria for this function:
#
# Marks for this function are allocated as follows:
#
# 1 mark: the function signature is correct
# 1 mark: the dictionary has been created and returned correctly
# 1 mark: the dictionary has been populated correctly
# Function: save
#
# Requirements:
# [1] The function should be named save.
# [2] The function should have 1 parameter named quotes which represents a dictionary of phrases
# [3] The function should start by opening the file "quotes.txt" in write mode.
# [4] For each item in the dictionary quotes, the function should do the following:
# [5]    Write the item to the file on a new line and in the form "{friend}: {quote}" where a friend is the key and quote is the value stored in the dictionary.
# [6] Finally, you should ensure that the file is closed if it is not automatically closed.






            # f.write(k + ',' + v + '\n')
# The following additional code can be used to test your function:
#

#
# The function should create a file named quotes.txt which contains the following:
# Scooby Doo: Scooby Dooby Doo!
# Shaggy Rogers: Zoinks!
# Fred Jones: Hold the phone!
# Daphne Blake: Jeepers!
# Velma Dinkley: Jinkies!
#
# The assessment criteria for this function are shown below.  You should use this to check that you have met all the criteria for this function:
#
# Marks for this function are allocated as follows:
#
# 1 mark: the function signature is correct
# 1 mark: correctly opens the file in write mode
# 1 mark: correctly iterates through each item of the dictionary
# 1 mark: the file contains the correct output

def gang():
    print("Loading gang...")
    friends = ['Scooby Doo', 'Shaggy Rogers', 'Fred Jones', 'Daphne Blake', 'Velma Dinkley']
    print(friends)
    print("...Done!")
    return friends

# gang()

def phrases(friends):
    quotes = {}
    for friend in friends:
        print(f"What does {friend} say?")
        quote = input()
        quotes[friend] = quote
    return quotes

friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")

def save(quotes):
    file = open('quotes.txt','w')
    for friend, quote in quotes.items():
    # for friend, quote in enumerate(quotes):
        file.write(f'{friend}: {quote}\n')



save(quotes)
print("The file contains...")
file = open("quotes.txt")
print(file.read())
file.close()

