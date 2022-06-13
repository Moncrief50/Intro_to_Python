# Problem(1): Roots
# Compute and print both roots of the quadratic equation x2-5.86 x+ 8.5408.
import math
def get_roots():
          print("Input the a,b, & c values of the quadratic equation :")

          a = float(input("a = "))
          b = float(input("b = "))
          c = float(input("c = "))
          E = b**2 - 4 * a * c
          R1 = (-b + math.sqrt(E)) / (2 * a)
          R2 = (-b - math.sqrt(E)) / (2 * a)

          print("Positive Root = ", round(R1, 4))
          print("Negative Root = ", round(R2, 4))

get_roots()

# Problem(2): Reciprocals
# Use a for loop to print the decimal representations of 1/2, 1/3, ..., 1/10, one on each line.

def get_decimal():
    print(" Step 2: Find the Reciprocals")

    for i in range(2,11):
       print(f"1/{i} = ", 1/i, end =  "\n")

get_decimal()