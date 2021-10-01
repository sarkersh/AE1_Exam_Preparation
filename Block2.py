def gang():
    print("Loading gang...")
    listNames = ['Scooby Doo', 'Shaggy Rogers', 'Fred Jones', 'Daphne Blake', 'Velma Dinkley']
    print(listNames)
    print("...Done!")
    return listNames


def phrases(friends):
    myDict = {}
    for friend in friends:
        user = input("What does {friend} say?\n")
        # myDict(key)=user
        key = str(friend)
        myDict.setdefault(key, [])
        myDict[key].append(str(user))

    return myDict


friends = gang()
quotes = phrases(friends)
print(f"\nPhrases: {quotes}\n")


def save(quotes):
    f = open(quotes)
    for index, item in enumerate(quotes):
        f.write(index, item)
    f.close()

save(quotes)