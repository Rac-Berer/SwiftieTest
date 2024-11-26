# 1. Prompt for favorite artist:
# Set variable and start it at 0
artist = input("Who's your Favorite Artist? ").lower()
result = 0

names = {
    "taylor swift": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "taylor": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "tay": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "tay swift": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "t swift": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "swifty": (1, "You've scored a Blank Space on the scoreboard! One point for you!\n1, 2, 3, Let's go, Bitch!"),
    "t-sweezy": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "tsweezy": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "t sweezy": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "t-swizzle": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "t swizzle": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!"),
    "tswizzle": (2, "You've scored a Blank Space on the scoreboard! One point for good taste and another for knowing her Rap name!")
}

if artist in names:
    points, message = names[artist]
    result += points
    print(message)
    if points == 2:
        name = input("Hey, it's a thug story. Now tell 'em who you are ").capitalize()
        print(f"1, 2, 3, Let's go, {name}!")
else:
    print("That's cool, but this is about Taylor Swift")
print("You have " + str(result) + " points so far!")


# 2. Using match/case for first song written
firstSong = input("What was the first song she wrote? ").lower()
match firstSong:
    case "lucky you":
        result += 1
        print("Nailed it! Just like a Love Story! You're Enchanted to score that point!")
    case "tim mcgraw":
        result = result
        print("'Tim McGraw' was not Taylor Swift's first written song, but it was her first released single. 'Lucky You' was the first song she wrote.")
    case _:
        result = result
        print("Nice try, but I knew you were Trouble when you said that! Actually, 'Lucky You' was her first written song. Shake it off and try again later!")
print("You have " + str(result) + " points so far!")

# 3. The age when Taylor wrote her first song.
age = input("How old was she when she wrote 'Lucky You'? ").lower()
if age == "12" or age == "twelve":
    result += 1
    print("Yes, only 12 years old. What a mastermind!")
else:
    result = result
    print("Not really, but you've got this, just breathe")

print("You have " + str(result) + " points so far!")


# 4. Using if/else for middle name
middleName = input("What is Taylor's middle name? ").lower()
if middleName == "alison":
    result += 1
    print("Correct! It's like we're living in a fairy tale!")
elif middleName == "allison":
    print("You're almost there, just a few notes off!")
else:
    print("That answer wasn’t Ready for It, but keep going!")

print("You have " + str(result) + " points so far!")


# 5. Prompt for Taylor's birthdate
# import datetime
from datetime import datetime

# Formats to recognize various date inputs
birthdayFormats = [
    "december 13 1989",
    "dec 13 1989",
    "13 december 1989",
    "13 dec 1989",
    "13 of december 1989",
    "13 of dec 1989",
    "december 13th 1989",
    "dec 13th 1989",
    "12/13/1989",
    "13/12/1989",
    "1989 december 13",
    "1989 dec 13",
    "1989 13 december",
    "1989 13 dec",
    "1989 december 13th",
    "1989 dec 13th"
]

# Formats without year
birthdayNoYear = [
    "december 13",
    "dec 13",
    "13th of december",
    "13th of dec",
    "13 of december",
    "13 of dec",
    "december 13th",
    "dec 13th",
    "12/13",
    "13/12"
]



while True:
    dateInput = input("When was Taylor born? ").lower().replace(",", "").replace(".", "").strip()
    
    if any(dateInput == birthday for birthday in birthdayFormats):
        print("Another point for you! We’re feeling 22!")
        result += 1
        break
    elif any(dateInput == birthday for birthday in birthdayNoYear):
        year_input = input("Yes, but what year? ").strip()
        if year_input == "1989":
            print("You're right, that answer will never go out of Style!")
            result += 1
            break
        else:
            print("No, but I'll give you a hint, it's the name of her 5th album!")
    elif dateInput == "1989":
        dateInput2 = input("That's the year but what day? ").lower().replace(",", "").replace(".", "").strip()
        if any(dateInput2 == birthday for birthday in birthdayNoYear):
            result += 1
            print("That’s a hit! You get a point for style and grace!")
            break
        else:
            print("Incorrect, but hey, you're fearless, keep going!")
    else:
        print("Incorrect, but hey, you're fearless, keep going!")

print("You have " + str(result) + " points so far!")







# 6. Initialize the list of Taylor Swift's cats and while loop for guesses
catNames = ["olivia benson", "detective olivia benson", "meredith grey", "benjamin button"]

while catNames:
    cat = input("Can you name each of Taylor's cats? ").lower()
    if cat in catNames:
        catNames.remove(cat)
        print(f"Flawless, {cat.title()} is one of her furbabies, can you guess all of them?")
        if cat == "olivia benson" or cat == "detective olivia benson":
            if "olivia benson" in catNames:
                catNames.remove("olivia benson")
            if "detective olivia benson" in catNames:
                catNames.remove("detective olivia benson")
            result +=1
    elif cat == "olivia" or cat == "meredith" or cat == "benjamin":
        print("Almost there, but not quite hitting the high note meow! type 'SETKAM' to skip.")
    elif cat == "setkam":
        print("Until next time—meow you later!")
        break
    else:
        print(f"Sorry, {cat} isn't one of them. Shake it off and try again. If you want to skip this, enter 'SETKAM'.")

if not catNames:
    print("Congratulations! You've guessed them all!")
print("You have " + str(result) + " points so far!")



# 7. Name her parents
parents = ["andrea finlay", "andrea", "scott kingsley swift", "scott swift", "scott kingsley", "scott"]

while parents:
    parent = input("Do you know her parents' names? ").lower()
    if parent in parents:
        parents = [p for p in parents if parent not in p]
        if "andrea" in parent:
            result += 1
            print(f"You're The Man! {parent.title()} is her mother")
            parents.remove(parent)
        elif "scott" in parent:
            result += 1
            print(f"You're The Man! {parent.title()} is her father")

    elif "andrea" in parent and "scott" in parent:
        result += 2
        print(f"You're The Man! Her parents are indeed Andrea and Scott!")
        break
    elif parent == "thebestday":
        print("Have yourself The Best Day!")
        break
    else:
        print("I think there's been a Glitch! Maybe try something else next time. Type 'TheBestDay' if you want to skip")
print("You have " + str(result) + " points so far!")



# 8. Early Inspiration
influences = ["the chicks", "shania twain", "tim mcgraw"]
while influences:
    influence = input("Who were early Insperations for Taylor starting country music? ").lower()
    if influence in influences:
        influences = [p for p in influences if influence not in p]
        result += 1
        print("You’re right, you never go out of Style!")
    elif influence == '2006':
        print("Teardrops on my Quiz!")
        break    
    else:
        print("Oops, not quite, shake it off and try again! Type '2006' to skip")
print("You have " + str(result) + " points so far!")


# 9. Instruments Taylor plays:
instruments = ["guitar", "piano", "ukulele", "electric guitar", "banjo"]

while instruments:
    instrument = input("What instruments does Taylor know how to play? ").lower()
    if instrument in instruments:
        instruments.remove(instrument)
        print("That’s spot-on! You earned a point, superstar!")
        result += 1
    elif instrument == "talented":
        print("Hell yeah she's talented, but onto the next question.")
    else:
        print(f" Sorry, {instrument} is not one (that I know of). Type 'talented' to stop guessing.")

print("You have " + str(result) + " points so far!")

# 10. Favorite Dessert (mine too)
dessert = input("What is Taylor's favorite dessert? ").lower()
match dessert:
    case "cheesecake":
        result +=1
        print("Aren't you sweeter than sweet tea in the summer, another point for you!")
    case _:
        print("Not according to my source, however I unfortunately don't personally know Taylor.")
print("You have " + str(result) + " points so far!")


# 11. Awards throughout her career
awards = int(input("How many awards has Taylor won throughout her career? "))

match awards:
    case 540:
        print("You're Enchanted to score that point!")
        result += 1
    case _ if awards < 540:
        print("Maybe at one point, but more now.")
    case _ if awards > 540: 
        print("Maybe by now, but not when this quiz was created.")
    case _:
        print("You missed it - Look what you made me do!")




# 12. Go to fast food order
# fastFood = ["cheeseburger", "fries", "chocolate shake"]
