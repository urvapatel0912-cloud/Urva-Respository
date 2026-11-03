#Write a program that asks the user for the length and width of a rectangle.
#The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of all four sides.

#P=2(l+w)
#a=l*w

len = float(input("Enter a length of rectangle: "))
Width = float(input("Enter a width of rectangle: "))
perimeter= float(2*(len + Width))
Area=float(len * Width)
print(f"Perimeter: {perimeter}")
print(f"Area: {Area}")
