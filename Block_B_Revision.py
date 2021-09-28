"""Create 3 functions: pokes
•	start by displaying the message “Here are the Pokemon!”
•	create a list named me_poke
•	populate the list with these strings:
“Pikachu”
“Muk”
“Arbok”
“Charmander”
“Mewtoo”
“Ratatata”
“Muk”
•	display the full list, with each name printed on the same line, separated by three asterisks
•	return the list
sounds
•	a single parameter named p should be passed to this function; p is a list of pokemon
•	create a dictionary called noises
•	for every pokemon in p, ask user to enter the sound that particular pokemon makes
•	store the sound with the pokemon’s name within noises
•	return noises
store
•	takes in one parameter named sounds which is a dictionary of pokemon sounds
•	the function should open the file “pok_sounds.csv” in suitable mode
•	for each entry in sounds, the function should allocate all pokemon names in one column with pokemon
sounds in the other column, so to preserve the correct name-sound combination
•	ensure the file is closed if it’s not being closed automatically"""


def pokes():
    print("Here are the Pokemon!")
    me_poke = ["Pikachu", "Muk", "Arbok", "Charmander", "Mewtoo", "Ratatata", "Muk"]
    for pokemon in me_poke:
        print(pokemon, end="***")
    return me_poke


# pokes()
def sounds(p):
    noises = {}
    for p_noise in p:
        noise = input(f"Please enter the noise for pokemon {p_noise}: ").split(",")
        noises[p_noise] = noise
    print(noises)
    return noises


sounds(['Pikacu', 'Abrakadabra'])
