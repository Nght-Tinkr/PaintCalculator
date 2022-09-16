# 1 litre of paint approx 15sqm
print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")


wallWidth = int(input("Please enter the width of the wall you want to paint in meters: "))
wallHeight = int(input("Please enter the height of the wall you want to paint in meters: "))
wallCoatAmount = int(input("Please enter how many coats of paints you would like on your wall: "))
#obstructions = input("Are there any obstructions on the wall you do not wish to paint over? (Y/N)")

i = 0
while i < 2:
        obstructions = input("Are there any obstructions on the wall you do not wish to paint over? e.g.door, window (Y/N): ")
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

obstructionSurfaceArea = obstructionsHeight * obstructionsWidth
wallSurfaceArea = wallHeight * wallWidth
wallSurfaceAreaObstruction = wallSurfaceArea - obstructionSurfaceArea





if obstructionTrue == True:
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

    wallPaintOneCoat = int(wallSurfaceArea)/15

    wallPaintOneCoat = round(wallPaintOneCoat, 2)

    if wallCoatAmount > 1:
        wallPaintMultipleCoats = wallPaintOneCoat*wallCoatAmount
        print("Since your wall is", wallSurfaceArea, "sqm, with", wallCoatAmount, "coats, you will need", wallPaintMultipleCoats, "Litres of paint")
    else:
        print("since your wall is", wallSurfaceArea,"sqm, with 1 coat, you will need", wallPaintOneCoat, "Litres of paint.")
