# #Object Oriented Programming OOP
# from turtle import Turtle, Screen
# #from the turtle module, import Turtle class

# timmy = Turtle()
# #create a Turtle object
# print(timmy)

# timmy.shape("turtle")

# timmy.color("red", "blue")

# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Name",["Pikachu", "Charizard", "Wartortle"])
table.add_column("Type",["Electric", "Fire", "Water"])
table.align = "l"
table.border = True

print(table)