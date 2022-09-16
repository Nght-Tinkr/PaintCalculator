# 1 litre of paint approx 15sqm
print("Hello, Thank you for using Einars Paint Calculator. \nPlease enter the following information:")
wallWidth = int(input("Please enter the width of the wall you want to paint in meters: "))
wallHeight = int(input("Please enter the height of the wall you want to paint in meters: "))
wallCoatAmount = int(input("Please enter how many coats of paints you would like on your wall: "))

wallSurfaceArea = wallHeight * wallWidth

print("The surface area of your wall is", str(wallSurfaceArea) + "sqm")

wallPaintOneCoat = int(wallSurfaceArea)/15

wallPaintOneCoat = round(wallPaintOneCoat, 2)

print("It takes approximately 1L of paint to paint 15sqm of a wall with one coat")

if wallCoatAmount > 1:
    wallPaintMultipleCoats = wallPaintOneCoat*wallCoatAmount
    print("Since your wall is", wallSurfaceArea, "sqm, with", wallCoatAmount, "coats, you will need", wallPaintMultipleCoats, "Litres of paint")
else:
    print("since your wall is", wallSurfaceArea,"sqm, with 1 coat, you will need", wallPaintOneCoat, "Litres of paint.")
    