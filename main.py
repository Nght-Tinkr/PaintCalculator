# 1 litre of paint approx 15sqm
print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")

# i = 0
# while i < 2:
#     roomNumber = input(
#         "Are all the walls you intend to paint in the same room? Answer yes if only painting 1 wall (Y/N)")
#     if any(roomNumber.lower() == f for f in ["yes", "y", "Yes", "Y"]):
wall_surface_area = 0

i = 0
while i < 2:
    wall_amount = int(input("Please input the amount of walls you wish to paint "))
    if wall_amount > 0:
        break
    else:
        i += 1
        if i < 2:
            print("Please enter a valid number of walls")
        else:
            print("I'm sorry I cannot help you any further, please restart if you want to try again")
            quit()

for i in range(wall_amount):
    wallHeight = float(input("Please enter the height of the wall you want to paint in meters: "))
    wallWidth = float(input("Please enter the width of the wall you want to paint in meters: "))
    wall_surface_area = wall_surface_area + (wallWidth * wallHeight)
    #     i = 0
    #     while i < 2:
    #         wallAmount = input("Please enter the number of walls you are painting: (1-4)")
    #         if any(wallAmount.lower() == f for f in ["1"]):
    #             wallNumber = 1
    #             wallHeight = int(input("Please enter the height of the wall you want to paint in meters: "))
    #             wallWidth = int(input("Please enter the width of the wall you want to paint in meters: "))
    #             break
    #         elif any(wallAmount.lower() == f for f in ["2"]):
    #             wallNumber = 2
    #             wallHeight = int(input("Please enter the height of the room you want to paint in meters: "))
    #             wallWidth1 = int(input("Please enter the width of the first wall you want to paint in meters: "))
    #             wallWidth2 = int(input("Please enter the width of the second wall you want to paint in meters"))
    #             break
    #         elif any(wallAmount.lower() == f for f in ["3"]):
    #             wallNumber = 3
    #             wallHeight = int(input("Please enter the height of the room you want to paint in meters: "))
    #             wallWidth1 = int(input("Please enter the width of the first wall you want to paint in meters: "))
    #             wallWidth2 = int(input("Please enter the width of the second wall you want to paint in meters"))
    #             wallWidth3 = int(input("Please enter the width of the third wall you want to paint in meters"))
    #             break
    #         elif any(wallAmount.lower() == f for f in ["4"]):
    #             wallNumber = 4
    #             wallHeight = int(input("Please enter the height of the room you want to paint in meters: "))
    #             wallWidth = int(input("Please enter the width of the room you want to paint in meters: "))
    #             wallLength = int(input("Please enter the length of the room you want to paint in meters: "))
    #             break
    #         else:
    #             i += 1
    #             if i < 2:
    #                 print("Please enter the amount of rooms you have to paint")
    #             else:
    #                 print("I'm sorry I cannot help you any further, please restart if you want to try again")
    #                 quit()
    #     break
    # elif any(roomNumber.lower() == f for f in ["no", "No", "n", "N"]):
    #     print("Sorry this hasn't been coded in yet")
    #     break
    # else:
    #     i += 1
    #     if i < 2:
    #         print("Please enter yes or no")
    #     else:
    #         print("I'm sorry I cannot help you any further, please restart if you want to try again")
    #         quit()




i = 0
while i < 2:
    obstruction_amount = int(input("Please enter the amount of obstructions on any of the walls "))
    if obstruction_amount == 0:
        obstruction_true = False
        break
    elif obstruction_amount > 0:
        obstruction_true = True
        break
    else:
        i += 1
        if i < 2:
            print("Please enter a valid number")
        else:
            print("I will assume there are no obstructions")
            obstruction_true = False
obstruction_surface_area = 0
if obstruction_true == True:
    for i in range(obstruction_amount):
        obstruction_height = float(input("Please enter the height of the obstruction you want to paint in meters: "))
        obstruction_width = float(input("Please enter the width of the obstruction you want to paint in meters: "))
        obstruction_surface_area = obstruction_surface_area + (obstruction_height * obstruction_width)
else:
    pass

    # if any(obstructions.lower() == f for f in ["yes", "y", "Yes", "Y"]):
    #     obstruction_true = True
    #     obstructions_width = int(input("What is the width of your obstruction in meters: "))
    #     obstructions_height = int(input("What is the height of your obstruction in meters: "))
    #     obstruction_surface_area = obstructions_height * obstructions_width
    #     # return obstruction_surface_area, obstruction_true
    #
    #     break
    # elif any(obstructions.lower() == f for f in ["no", "No", "n", "N"]):
    #     obstruction_true = False
    #     # return obstruction_true
    #     break
    # else:
    #     i += 1
    #     if i < 2:
    #         print("Please enter yes or no")
    #     else:
    #         print("I will assume there are no obstructions")


wall_coat_amount = int(input("Please enter how many coats of paints you would like on your wall: "))




# if wallNumber == 1:
#     wall_surfacearea = wallHeight * wallWidth
#     # return wall_surfacearea
# elif wallNumber == 2:
#     wall_surfacearea = wallHeight * (wallWidth1 + wallWidth2)
#     # return wall_surfacearea
# elif wallNumber == 3:
#     wall_surfacearea = wallHeight * (wallWidth1 + wallWidth2 + wallWidth3)
#     # return wall_surfacearea
# else:
#     wall_surfacearea = wallHeight * (2 * (wallWidth + wallLength))
#     # return wall_surfacearea

#   obstructions = input("Are there any obstructions on the wall you do not wish to paint over? (Y/N)")


"""i = 0
while i < 2:
    obstructions = input(
        "Are there any obstructions on the wall you do not wish to paint over? e.g.door, window (Y/N): ")
    if any(obstructions.lower() == f for f in ["yes", "y", "Yes", "Y"]):
        obstructionTrue = True
        obstructionsWidth = int(input("What is the width of your obstruction in meters: "))
        obstructionsHeight = int(input("What is the height of your obstruction in meters: "))

        break
    elif any(obstructions.lower() == f for f in ["no", "No", "n", "N"]):
        obstructionTrue = False
        break
    else:
        i += 1
        if i < 2:
            print("Please enter yes or no")
        else:
            print("I will assume there are no obstructions")
"""

"""if wallNumber == 1:
    wallSurfaceArea = wallHeight * wallWidth
elif wallNumber == 2:
    wallSurfaceArea = wallHeight * (wallWidth1 + wallWidth2)
elif wallNumber == 3:
    wallSurfaceArea = wallHeight * (wallWidth1 + wallWidth2 + wallWidth3)
else:
    wallSurfaceArea = wallHeight * (2 * (wallWidth + wallLength))
"""

if obstruction_true == True:
    # obstructionSurfaceArea = obstructions_height * obstructions_width
    wallSurfaceAreaObstruction = wall_surface_area - obstruction_surface_area
    print("The surface area of your wall with the obstruction is", str(wallSurfaceAreaObstruction) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")
    wallPaintOneCoat = int(wallSurfaceAreaObstruction) / 15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wall_coat_amount > 1:
        wallPaintMultipleCoats = wallPaintOneCoat * wall_coat_amount
        print("Since your wall is", wallSurfaceAreaObstruction, "sqm, with", wall_coat_amount, "coats, you will need",
              wallPaintMultipleCoats, "Litres of paint")
    else:
        print("since your wall is", wallSurfaceAreaObstruction, "sqm, with 1 coat, you will need", wallPaintOneCoat,
              "Litres of paint.")
else:
    print("The surface area of your wall is", str(wall_surface_area) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")

    wallPaintOneCoat = int(wall_surface_area) / 15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wall_coat_amount > 1:
        wallPaintMultipleCoats = wallPaintOneCoat * wall_coat_amount
        print("Since your wall is", wall_surface_area, "sqm, with", wall_coat_amount, "coats, you will need",
              wallPaintMultipleCoats, "Litres of paint")
    else:
        print("since your wall is", wall_surface_area, "sqm, with 1 coat, you will need", wallPaintOneCoat,
              "Litres of paint.")
