# # Prompt for favorite artist and match/case solution:
# # Set variable and start it at 0
artist = input("Who's your Favorite Artist? ").lower()
result = 0

actions = {
    "taylor swift": (1, "You get a point for good taste!\n1, 2, 3, Let's go, Bitch!"),
    "taylor": (1, "You get a point for good taste!\n1, 2, 3, Let's go, Bitch!"),
    "tay": (1, "You get a point for good taste!\n1, 2, 3, Let's go, Bitch!"),
    "t swift": (1, "You get a point for good taste!\n1, 2, 3, Let's go, Bitch!"),
    "t-sweezy": (2, "You get a point for good taste and a bonus one for knowing her rap name!"),
    "tsweezy": (2, "You get a point for good taste and a bonus one for knowing her rap name!"),
    "t sweezy": (2, "You get a point for good taste and a bonus one for knowing her rap name!")
}

if artist in actions:
    points, message = actions[artist]
    result += points
    print(message)
    if points == 2:
        name = input("Hey it's a thug story now tell them who you are ")
        print(f"1, 2, 3, Let's go, {name}!")
else:
    print("That's cool, but this is about Taylor Swift")

value = input("What was the first song she wrote? ").lower()
match value:
    case "lucky you":
        result += 2
        age = input("And how old was she when she wrote it? ")
        match age:
            case 12 | "Twelve" | "twelve":
                result += 1
            case _:
                result = result
    case "Tim McGraw":
        result += 1
        print("Not exactly, but that was her first hit song, so I'll give you a point for it.")
    case _:
        result = result
print("You have " + str(result) + " points so far!")

value = input("Who interrupted Taylor's acceptance speech when she was still just a teen? " )
match value.title():
    case "Kanye West" | "kanye west" | "KANYE WEST" | "Kanye west" | "kanye West":
        result = result + 1
        print("Yep, that's the one.")
    case "Kanye" | "kanye" | "KANYE":
        result = result + 1
        print("Yep, that's the one.")
    case _:
        result = result
        print("Sorry, that's not it.")
print("You have " + str(result) + " points so far!")


