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
