# Karter Ence
# Shape Size Calculations (Redux)
# 9/11/2019
def square():
# Get side lengths for square/rectangle
    print("What is the length of the square?")
    sqrLength = float(input(": "))
    print("What is the width of the square?")
    sqrWidth = float(input(": "))
    # Calculate perimeter and area
    sqrPer = (sqrLength +sqrWidth) * 2
    sqrArea = sqrLength * sqrWidth
    # Print the calculations
    print(str.format("The perimeter of the square is {0:.2f}", sqrPer))
    print(str.format("The area of the square is {0:.2f}", sqrArea))
    # ASCII with side lengths
    print(str.format("""
            {0:^10.2f}
     _________________________
    |                         |
    |                         |
    |                         |
    |                         |
    |                         | {1:^10.2f}
    |                         |
    |                         |
    |                         |
    |                         |
    |_________________________|
    """, sqrLength, sqrWidth))
def curcal():
    # Get the radius of the circle
    print("What is the radius of the circle?")
    radius = float(input(": "))
    # Calculate the circumference
    circumference = 2 * 3.14 * radius
    print(str.format("The circumference of the circle is {0:.2f}", circumference))
    # ASCII art with radius
    print(str.format("""
               %%%    %%%
          %%%              %%%

      %%%                      %%%
            {0:^12.2f}     
     %%% __________0             %%%
        
     %%%                         %%%

     %%%                        %%%

        %%%                  %%%

              %%%     %%%
    """, radius))
def triangle():
    # Get the base and height of the triangle
    print("What is the base length of the triangle?")
    triBase = float(input(": "))
    print("What is the height of the triangle?")
    triHeight = float(input(": "))
    # Calculate the area of the triangle
    triArea = (triBase * triHeight) / 2
    print(str.format("The area of the triangle is {0:.2f}",triArea))
    # ASCII are with base and height
    print(str.format("""
           /|
          / |
         /  |
        /   |
       /    | {0:<12.2f}
      /     |
     /      |
    /_______|
    {1:^12.2f}  
    """, triHeight, triBase))
def cube():
    # Get the measurements of the cube/rectangular prism
    print("What is the height of the cube?")
    cubeHeight = float(input(": "))
    print("What is the length of the cube?")
    cubeLength = float(input(": "))
    print("What is the width of the cube?")
    cubeWidth = float(input(": "))
    # Calculate and print the volume
    cubeVol = cubeHeight * cubeLength * cubeWidth
    print(str.format("The volume of the cube is {0:.2f}", cubeVol))
    # ASCII art with measurements
    print(str.format("""
    {0:^15.2f}
       +--------+
      /        /|
     /        / | {1:<15.2f}
    +--------+  |
    |        |  |
    |        |  +
    |        | /
    |        |/{2:<14.2f}
    +--------+
    """, cubeLength, cubeHeight, cubeWidth))




def intro():
    print("""


   Welcome yo my homwork assiment please chose a option



     1: option 1
     2: option 2
     3: option 3
     4: option 4
     """)

def option1():
    print("square")
def option2():
    print("square")
def option3():
    print("triangle")
def option4():
    print("cube")


def anwser():
    while True:
        intro()
        choice =input(" pick a number between 1 and 4")
        if choice =="1":
            square()
        elif choice =="2":
            curcal()
        elif choice =="3":
            triangle()
        elif choice =="4":
            cube()
      


answer()
