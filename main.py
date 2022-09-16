# 1 litre of paint approx 15sqm
print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")
wallWidth = int(input("Please enter the width of the wall you want to paint in meters: "))
wallHeight = int(input("Please enter the height of the wall you want to paint in meters: "))

wallSurfaceArea = wallHeight * wallWidth

print("The surface area of your wall is", str(wallSurfaceArea) + "sqm")

wallPaintOneCoat = int(wallSurfaceArea)/15

wallPaintOneCoat = round(wallPaintOneCoat, 2)

print("It takes approximately 1L of paint to paint 15sqm of wall with one coat, since your wall is", wallSurfaceArea, "You will need", str(wallPaintOneCoat) + "L of paint.")