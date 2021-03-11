x1,y1,z1=tuple(map(float,(input("Enter point 1 (without brackets): ")).split(",")))
x2,y2,z2=tuple(map(float,(input("Enter point 2 (without brackets): ")).split(",")))

print("\n")

dist=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)**0.5

print("distance between the points are: ",dist)