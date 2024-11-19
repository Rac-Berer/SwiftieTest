# Prompt for favorite artist:
# Set variable and start it at 0
artist = input("Who's your Favorite Artist? ").lower()
result = 0

actions = {
    "taylor swift": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "taylor": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "tay": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "t swift": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "t-sweezy": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "tsweezy": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "t sweezy": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "t-swizzle": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "t swizzle": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "tswizzle": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!")
}

if artist in actions:
    points, message = actions[artist]
    result += points
    print(message)
    if points == 2:
        name = input("Hey, it's a thug story. Now tell 'em who you are ").capitalize()
        print(f"1, 2, 3, Let's go, {name}!")
else:
    print("That's cool, but this is about Taylor Swift")
print("You have " + str(result) + " points so far!")


# 1. Using match/case for first song written
firstSong = input("What was the first song she wrote? ").lower()
match firstSong:
    case "lucky you":
        result += 2
        print("Nailed it! Just like a Love Story! You're Enchanted to score that point!")
    case "tim mcgraw":
        result = result
        print("'Tim McGraw' was not Taylor Swift's first written song, but it was her first released single. 'Lucky You' was the first song she wrote.")
    case _:
        result = result
        print("Nice try, but I knew you were Trouble when you said that! Actually, 'Lucky You' was her first written song. Shake it off and try again later!")
print("You have " + str(result) + " points so far!")

# 2. The age when Taylor wrote her first song.
age = input("How old was she when she wrote 'Lucky You'? ").lower()
if age == "12" or age == "twelve":
    result += 1
    print("Yes, only 12 years old. What a mastermind!")
else:
    result = result
    print("Not really, but you've got this, just breathe")

print("You have " + str(result) + " points so far!")


# 3. Using if/else
middleName = input("What is Taylor's middle name? ").lower()
if middleName == "alison":
    result += 1
    print("Correct! It's like we're living in a fairy tale!")
else:
    print("That answer wasn’t Ready for It, but keep going!")

print("You have " + str(result) + " points so far!")


# 4. Handling interruption question
interruption = input("Who interrupted Taylor's acceptance speech when she was still just a teen? ").lower()
match interruption:
    case "kanye west" | "kanye":
        result += 1
        print("You’re right, you never go out of Style!")
    case _:
        result = result
        print("Oops, not quite, you need to shake it off and try again!")
print("You have " + str(result) + " points so far!")


# 5. Handling false endorsement question
falseEndorse = input("Who posted AI of Taylor falsely endorsing them? ").lower()
match falseEndorse:
    case "donald trump" | "trump":
        result += 1
        print("That’s spot-on! You earned a point, superstar!")
    case _:
        print("Sorry, that’s not correct. The right answer is Donald Trump. This led to her publicly sharing who she was voting for.")
print("You have " + str(result) + " points so far!")
