x=int(input("Podaj x:"))
y=int(input("Podaj y:"))
z=int(input("Podaj z:"))

if (x > y and x > z):
      if (y > z):
        print(f"Kolejność: {z}, {y}, {x}")
      else:
        print(f"Kolejność: {y}, {z}, {x}")
elif(y > x and y > z):
      if (x > z):
        print(f"Kolejność: {z}, {x}, {y}")
      else:
        print(f"Kolejność: {x}, {z}, {y}")
elif (z > x and z > y):
      if (x > y):
        print(f"Kolejność: {y}, {x}, {z}")
      else:
        print(f"Kolejność: {x}, {y}, {z}")
