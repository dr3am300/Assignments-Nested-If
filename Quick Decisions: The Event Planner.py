# Objective:
# To practice the use of shorthand if statements in determining event-related decisions.
# Task 1: Code Correction
# You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

# Buggy Code:

# attendees = input("Enter number of attendees: ")
# venue = "large hall" if attendees > 100 else "conference room"
# print(venue)

# Corrected code

attendees = int(input("Enter number of attendees: "))

if attendees >= 100:
    venue = "large hall"
else:
    venue = "conference room"
print(venue)

# Task 2: Venue Selection
# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.
attendees = int(input("Enter number of attendees: "))

if attendees >= 100:
    venue = "large hall"
    facility = "projector"
else:
    venue = "conference room"
    facility = "audio system"
print(venue, facility)

# Task 3: Catering Choices
# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

attendees = int(input("Enter number of attendees: "))
food_choice = input("Do you want vegetarian food? (yes/no) ")

if attendees >= 100:
    if food_choice == "yes":
        venue = "large hall"
        facility = "projector"
        caterer = "Veggie Delight Caterers"
else:
    venue = "conference room"
    facility = "audio system"
    caterer = "Gourmet Meals Caterers"
print(venue, facility, caterer)

