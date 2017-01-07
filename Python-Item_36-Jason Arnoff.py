# Python:       2.7.13
# Author:       Jason Arnoff
# Purpose:      Tech Academy Drill
#               Python Course - Item 36

# Import sqrt from math, in order to use the sqr function
from math import sqrt


# Everything starts here
def start():
    name = getName()
    age = getAge(name)
    sr_age = sqrt(float(age))
    print("\nName = {}, Age = {}".format(name,age))
    print("\nThe square root of your age is {}.  That's probably useful to know, right?".format(sr_age))
    print("\nIf you think that was useless info, this might get painful!")
    print("In 5 years, you'll be {}. Last year, you were {}.".format(age + 5,age - 1))
    half_age = getHalfAge(age)
    print("Half your lifetime ago, you were {}{}. In twice your lifetime, you'll be {}.".format(age / 2,half_age,age * 2))
    next5years(age)
    canYouDrive(age)


# Get user's name.  Make sure it's not blank
def getName():
    name = raw_input("Hi there, what's your name? ")
    while name == "":
        name = raw_input("\nYou forgot to enter your name. What's your name? ")
    return name

# Get user's age.  Make sure it's not blank
def getAge(name):
    age = raw_input("Welcome {}! How old are you? ".format(name))
    while age == "":
        age = raw_input("\nYou forgot to enter your age. How old are you? ")
    return int(age)

# Get user's age over the next 5 years and print it to the screen
def next5years(age):
    you_next_five = ["next year","in 2 years","in 3 years","in 4 years","in 5 years"]
    age_next_five = []
    next_age = age
    for i in range(0,5):
        next_age += 1
        age_next_five.append(next_age);
        print("\nYour age {} will be {}.".format(you_next_five[i],age_next_five[i]))

# Check if the user's old enough to drive, or if they're age is too high to be real
def canYouDrive(age):
    if(age < 16):
        print("You aren't old enough to drive!")
    elif(age > 16 and age < 110):
        print("You are old enough to drive!")
    else:
        print("I think you might have lied about your age.")

# Check if they're age is even or odd, to see if they were X or X and a half half a lifetime ago
def getHalfAge(age):
    half_age = ""
    if(age % 2 == 1):
        half_age = " (and a half)"
    return half_age


            
if __name__ == "__main__":
    start()
