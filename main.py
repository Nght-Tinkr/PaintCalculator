import pandas as pd
import csv


# 1 litre of paint approx 15sqm

print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")

def error_handling_numbers(user_input):             #Defining an error handling function to check wether the input
    valid = False                                   # is a number
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
    wall_amount = int(error_handling_numbers(wall_amount))                  #calling the function defined previously


    if wall_amount > 0:
        break
    else:
        i += 1
        if i < 3:
            print("Please enter a valid number of walls")
        else:
            print("I'm sorry I cannot help you any further, please restart if you want to try again")
            quit()
# above code is giving the user an option to input information, if the input isnt valid it gives the user a chance to
# re-enter before quitting the program

colour_amount = 0
colours = ["red", "yellow", "green", "blue", "brown", "black", "white"]

red, yellow, green, blue, brown, black, white = 0, 0, 0, 0, 0, 0, 0
for i in range(wall_amount):
    wallHeight = input("Please enter the height of the wall number {} you want to paint in meters: ".format(i+1))
    wallHeight = float(error_handling_numbers(wallHeight))

    wallWidth = input("Please enter the width of the wall number {} you want to paint in meters: ".format(i+1))
    wallWidth = float(error_handling_numbers(wallWidth))


    print("Please pick the colour that most closely matches the colour you would like to paint your wall:")
    i = 0
    while i < 3:
        wallColour = input("Red, Yellow, Green, Blue, Brown, Black, White: ")
        wallColour = wallColour.lower()
        if wallColour in colours:
            match wallColour:
                case "red":
                    red = 1
                    colour_amount += 1
                    break
                case "yellow":
                    yellow = 1
                    colour_amount += 1
                    break
                case "green":
                    green = 1
                    colour_amount += 1
                    break
                case "blue":
                    blue = 1
                    colour_amount += 1
                    break
                case "brown":
                    brown = 1
                    colour_amount += 1
                    break
                case "black":
                    black = 1
                    colour_amount += 1
                    break
                case "white":
                    white = 1
                    colour_amount += 1
                    break
        else:
            i += 1
            if i < 3:
                print("Please enter a valid colour")
            else:
                print("I will assume theyre all the same colour")
                colour_amount += 1
                break



    wall_surface_area = wall_surface_area + (wallWidth * wallHeight)
    # above code is a loop that will update wall surface area variable depending on how many walls the user wants to paint


i = 0
while i < 3:
    obstruction_amount = input("Please enter the amount of obstructions on any of the walls, e.g. doors, windows ")
    obstruction_amount = int(error_handling_numbers(obstruction_amount))
    if obstruction_amount == 0:
        obstruction_true = False
        break
    elif obstruction_amount > 0:
        obstruction_true = True
        break
    else:
        i += 1
        if i < 3:
            print("Please enter a valid number")
        else:
            print("I will assume there are no obstructions")
            obstruction_true = False
# above code is giving the user an option to input information, if the input isnt valid it gives the user a chance to
# re-enter before quitting the program

obstruction_surface_area = 0
obstruction_counter = 0
if obstruction_true == True:
    for i in range(obstruction_amount):
        obstruction_counter = obstruction_counter + 1
        obstruction_height = input("Please enter the height of obstruction number {} you want to paint in meters: ".format(obstruction_counter))
        obstruction_height = float(error_handling_numbers(obstruction_height))
        obstruction_width = input("Please enter the width of obstruction number {} you want to paint in meters: ".format(obstruction_counter))
        obstruction_width = float(error_handling_numbers(obstruction_width))
        obstruction_surface_area = obstruction_surface_area + (obstruction_height * obstruction_width)
else:
    pass
# above code is a loop that will update obstruction surface area variable depending on how many obstructions there are

#how many coats the user wants for their wall
wall_coat_amount = input("Please enter how many coats of paints you would like on your wall: ")
wall_coat_amount = float(error_handling_numbers(wall_coat_amount))





if obstruction_true == True: #if there is an obstruction do following code
    wallSurfaceAreaObstruction = wall_surface_area - obstruction_surface_area
    print("The total surface area of your wall(s) with the obstruction(s) is", str(wallSurfaceAreaObstruction) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")
    wallPaintOneCoat = float(wallSurfaceAreaObstruction) / 15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wall_coat_amount > 1: #if there is more than one coat
        wallPaintMultipleCoats = wallPaintOneCoat * wall_coat_amount
        print("Since the total surface area of your wall(s) is", wallSurfaceAreaObstruction, "sqm, with", wall_coat_amount, "coats, you will need",
              wallPaintMultipleCoats, "Litres of paint in", colour_amount, "different colour(s)")
    else: #if there is only one coat
        print("since the total surface area of your wall(s) is", wallSurfaceAreaObstruction, "sqm, with 1 coat, you will need", wallPaintOneCoat,
              "Litres of paint in", colour_amount, "different colour(s)")
else: # if there was no obstruction
    print("The total surface area of your wall(s) is", str(wall_surface_area) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")

    wallPaintOneCoat = int(wall_surface_area) / 15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wall_coat_amount > 1:
        wallPaintMultipleCoats = wallPaintOneCoat * wall_coat_amount
        print("Since the total surface area your wall(s) is", wall_surface_area, "sqm, with", wall_coat_amount, "coats, you will need",
              wallPaintMultipleCoats, "Litres of paint in", colour_amount, "different colour(s)")
    else:
        print("since the total surface area of your wall(s) is", wall_surface_area, "sqm, with 1 coat, you will need", wallPaintOneCoat,
              "Litres of paint in", colour_amount, "different colour(s)")
