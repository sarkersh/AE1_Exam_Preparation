"""Create 3 functions:
fav_movie
•	asks the user what their favourite movie is
•	read user response
•	displays the message “{m} is terrible! How could you like it so much?” where m is the name of the movie provided by
 the user
imdb_rating
•	takes in one parameter named rating which represents a movie’s IMDB rating
•	function to check if the rating is above 7
•	displays “let’s watch it!” if rating is above 7
•	displays “not goanna waste my time on that!” if rating is 7 or below
•	displays “I hope you agree” at the end
binge
•	takes one parameter numb which represents the number of episodes in a series
•	for each episode, display “Oh-yeah!” on the screen, followed by “#n” where n is the current number of the episode
•	finally display “There are {u} episodes in the series” where u stands for the number of episodes in a series"""


def fav_movie():
    strUserInput = input("What's your favourite movie: ")
    print(f"{strUserInput} is terrible! How could you like it so much?")


# fav_movie()

def imdb_rating(rating):
    if (rating > 7):
        print("let’s watch it!")
    else:
        print("not goanna waste my time on that!")
    print("I hope you agree")


# imdb_rating(6)
# imdb_rating(7)
# imdb_rating(8)

def binge(numb):
    for n in range(numb):
        print(f"Oh-yeah!#{n+1}")
    print(f"There are {numb} episodes in the series")


# binge(7)
