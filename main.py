# 1 litre of paint approx 15sqm
print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")

i = 0
while i < 2:
    roomNumber = input(
        "Are all the walls you intend to paint in the same room? Answer yes if only painting 1 wall (Y/N)")
    if any(roomNumber.lower() == f for f in ["yes", "y", "Yes", "Y"]):
        i = 0
        while i < 2:
            wallAmount = input("Please enter the number of walls you are painting: (1-4)")
            if any(wallAmount.lower() == f for f in ["1"]):
                wallNumber = 1
                wallHeight = int(input("Please enter the height of the wall you want to paint in meters: "))
                wallWidth = int(input("Please enter the width of the wall you want to paint in meters: "))
                break
            elif any(wallAmount.lower() == f for f in ["2"]):
                wallNumber = 2
                wallHeight = int(input("Please enter the height of the room you want to paint in meters: "))
                wallWidth1 = int(input("Please enter the width of the first wall you want to paint in meters: "))
                wallWidth2 = int(input("Please enter the width of the second wall you want to paint in meters"))
                break
            elif any(wallAmount.lower() == f for f in ["3"]):
                wallNumber = 3
                wallHeight = int(input("Please enter the height of the room you want to paint in meters: "))
                wallWidth1 = int(input("Please enter the width of the first wall you want to paint in meters: "))
                wallWidth2 = int(input("Please enter the width of the second wall you want to paint in meters"))
                wallWidth3 = int(input("Please enter the width of the third wall you want to paint in meters"))
                break
            elif any(wallAmount.lower() == f for f in ["4"]):
                wallNumber = 4
                wallHeight = int(input("Please enter the height of the room you want to paint in meters: "))
                wallWidth = int(input("Please enter the width of the room you want to paint in meters: "))
                wallLength = int(input("Please enter the length of the room you want to paint in meters: "))
                break
            else:
                i += 1
                if i < 2:
                    print("Please enter the amount of rooms you have to paint")
                else:
                    print("I'm sorry I cannot help you any further, please restart if you want to try again")
                    quit()
        break
    elif any(roomNumber.lower() == f for f in ["no", "No", "n", "N"]):
        print("Sorry this hasn't been coded in yet")
        break
    else:
        i += 1
        if i < 2:
            print("Please enter yes or no")
        else:
            print("I'm sorry I cannot help you any further, please restart if you want to try again")
            quit()
wallCoatAmount = int(input("Please enter how many coats of paints you would like on your wall: "))
# obstructions = input("Are there any obstructions on the wall you do not wish to paint over? (Y/N)")

i = 0
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



if wallNumber == 1:
    wallSurfaceArea = wallHeight * wallWidth
elif wallNumber == 2:
    wallSurfaceArea = wallHeight * (wallWidth1 + wallWidth2)
elif wallNumber == 3:
    wallSurfaceArea = wallHeight * (wallWidth1 + wallWidth2 + wallWidth3)
else:
    wallSurfaceArea = wallHeight * (2 * (wallWidth + wallLength))



if obstructionTrue == True:
    obstructionSurfaceArea = obstructionsHeight * obstructionsWidth
    wallSurfaceAreaObstruction = wallSurfaceArea - obstructionSurfaceArea
    print("The surface area of your wall with the obstruction is", str(wallSurfaceAreaObstruction) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")
    wallPaintOneCoat = int(wallSurfaceAreaObstruction) / 15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wallCoatAmount > 1:
        wallPaintMultipleCoats = wallPaintOneCoat * wallCoatAmount
        print("Since your wall is", wallSurfaceAreaObstruction, "sqm, with", wallCoatAmount, "coats, you will need",
              wallPaintMultipleCoats, "Litres of paint")
    else:
        print("since your wall is", wallSurfaceAreaObstruction, "sqm, with 1 coat, you will need", wallPaintOneCoat,
              "Litres of paint.")
else:
    print("The surface area of your wall is", str(wallSurfaceArea) + "sqm")
    print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")

    wallPaintOneCoat = int(wallSurfaceArea) / 15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wallCoatAmount > 1:
        wallPaintMultipleCoats = wallPaintOneCoat * wallCoatAmount
        print("Since your wall is", wallSurfaceArea, "sqm, with", wallCoatAmount, "coats, you will need",
              wallPaintMultipleCoats, "Litres of paint")
    else:
        print("since your wall is", wallSurfaceArea, "sqm, with 1 coat, you will need", wallPaintOneCoat,
              "Litres of paint.")
