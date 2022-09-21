import pandas as pd
import csv
import pytest

# 1 litre of paint approx 15sqm

print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")


def error_handling_numbers(user_input):                             # Defining an error handling function to check whether the input
    valid = False                                                   # is a number
    while not valid:
        try:
            float(user_input)
            valid = True
            return user_input
        except ValueError:
            print("That is not a valid number, please enter a valid number")
            user_input = input()


wall_surface_area = 0

i = 0
while i < 3:
    wall_amount = input("Please input the amount of walls you wish to paint ")
    wall_amount = int(error_handling_numbers(wall_amount))          # calling the error handling function defined previously

    if wall_amount > 0:
        break
    else:
        i += 1
        if i < 3:
            print("Please enter a valid number of walls")
        else:
            print("I'm sorry I cannot help you any further, please restart if you want to try again")
            quit()
                                                                    # above code is giving the user an option to input
                                                                    # information, if the input isnt valid it gives the
                                                                    # user a chance to re-enter before quitting the program
colour_amount = 0
colours = ["red", "yellow", "green", "blue", "brown", "black", "white"]  # list of colours

red, yellow, green, blue, brown, black, white = 0, 0, 0, 0, 0, 0, 0  # setting colour variables as 0
for i in range(wall_amount):
    wall_height = input("Please enter the height of the wall number {} you want to paint in meters: ".format(i + 1))
    wall_height = float(error_handling_numbers(wall_height))        # calling error handling function

    wall_width = input("Please enter the width of the wall number {} you want to paint in meters: ".format(i + 1))
    wall_width = float(error_handling_numbers(wall_width))

    print("Please pick the colour that most closely matches the colour you would like to paint your wall:")
    i = 0
    while i < 3:                                                    # while loop to check input is correct
        wall_colour = input("Red, Yellow, Green, Blue, Brown, Black, White: ")
        wall_colour = wall_colour.lower()                           # setting the user input to be lower case so
        if wall_colour in colours:                                  # that it doesnt matter how the input is typed
            match wall_colour:
                case "red":                                         # match statements for what to do in each colour
                    if red == 0:
                        red = 1
                        colour_amount += 1
                        break
                    else:
                        break
                case "yellow":
                    if yellow == 0:
                        yellow = 1                                  #setting colour variable to 1 so that future iterations
                        colour_amount += 1                          #dont add to the colour_amount value, which is used
                        break                                       #later on to determine how many different colours you have used
                    else:
                        break
                case "green":
                    if green == 0:
                        green = 1
                        colour_amount += 1
                        break
                    else:
                        break
                case "blue":
                    if blue == 0:
                        blue = 1
                        colour_amount += 1
                        break
                    else:
                        break
                case "brown":
                    if brown == 0:
                        brown = 1
                        colour_amount += 1
                        break
                    else:
                        break
                case "black":
                    if black == 0:
                        black = 1
                        colour_amount += 1
                        break
                    else:
                        break
                case "white":
                    if white == 0:
                        white = 1
                        colour_amount += 1
                        break
                    else:
                        break
        else:
            i += 1
            if i < 3:
                print("Please enter a valid colour")
            else:
                print("I will assume theyre all the same colour")
                colour_amount += 1
                break

    wall_surface_area = wall_surface_area + (wall_width * wall_height)  #Updating total wall surface area upon each iteration


i = 0
while i < 3:
    obstruction_amount = input("Please enter the amount of obstructions on any of the walls, e.g. doors, windows ")
    obstruction_amount = int(error_handling_numbers(obstruction_amount))
    if obstruction_amount == 0:
        obstruction_true = False
        break
    elif obstruction_amount > 0:
        obstruction_true = True                                     # giving the user an option to input information,
        break                                                       # about obstructions, if the input isnt valid it gives the user a chance to
    else:                                                           # re-enter before quitting the program
        i += 1
        if i < 3:
            print("Please enter a valid number")
        else:
            print("I will assume there are no obstructions")
            obstruction_true = False


obstruction_surface_area = 0

if obstruction_true == True:                                        #Checking if obstruction is true from previous while loop
    for obstruction_counter in range(obstruction_amount):           #then asks you to input the dimensions of said obstructions

        obstruction_height = input(
            "Please enter the height of obstruction number {} you want to paint in meters: ".format(obstruction_counter + 1))
        obstruction_height = float(error_handling_numbers(obstruction_height))
        obstruction_width = input(
            "Please enter the width of obstruction number {} you want to paint in meters: ".format(obstruction_counter + 1))
        obstruction_width = float(error_handling_numbers(obstruction_width))
        obstruction_surface_area = obstruction_surface_area + (obstruction_height * obstruction_width)
else:
    pass                                                            # above code is a loop that will update obstruction surface area
                                                                    # variable depending on how many obstructions there are

wall_coat_amount = input("Please enter how many coats of paints you would like on your wall: ")     # how many coats the user wants for their wall
wall_coat_amount = float(error_handling_numbers(wall_coat_amount))  #calling error handling function

if obstruction_true == True:                                        # checking if there is an obstruction
    wall_surface_area_obstruction = wall_surface_area - obstruction_surface_area
    print("The total surface area of your wall(s) with the obstruction(s) is",
          str(wall_surface_area_obstruction) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")
    wall_paint_one_coat = float(wall_surface_area_obstruction) / 15

    wall_paint_one_coat = round(wall_paint_one_coat, 2)

    if wall_coat_amount > 1:                                        # checking if there is more than one coat
        wall_paint_multiple_coats = wall_paint_one_coat * wall_coat_amount
        print("Since the total surface area of your wall(s) is", wall_surface_area_obstruction, "sqm, with",
              wall_coat_amount, "coats, you will need",
              wall_paint_multiple_coats, "Litres of paint in", colour_amount, "different colour(s)")
    else:                                                           # if there is only one coat
        print("since the total surface area of your wall(s) is", wall_surface_area_obstruction,
              "sqm, with 1 coat, you will need", wall_paint_one_coat,
              "Litres of paint in", colour_amount, "different colour(s)")
else:                                                               # if there was no obstruction
    print("The total surface area of your wall(s) is", str(wall_surface_area) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")

    wall_paint_one_coat = int(wall_surface_area) / 15

    wall_paint_one_coat = round(wall_paint_one_coat, 2)

    if wall_coat_amount > 1:
        wall_paint_multiple_coats = wall_paint_one_coat * wall_coat_amount
        print("Since the total surface area your wall(s) is", wall_surface_area, "sqm, with", wall_coat_amount,
              "coats, you will need",
              wall_paint_multiple_coats, "Litres of paint in", colour_amount, "different colour(s)")
    else:
        print("since the total surface area of your wall(s) is", wall_surface_area, "sqm, with 1 coat, you will need",
              wall_paint_one_coat,
              "Litres of paint in", colour_amount, "different colour(s)")
