from prettytable import PrettyTable
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("burlywood", "burlywood4")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["electric", "Water", "Fire"])
# OR
table.field_names = ["Pokemon", "Type"]
table.add_row(["Marill", "Water"])
table.add_row(["Raichu", "Electric"])
table.align = "l"
table.add_autoindex("S:No.")
table.border = False 
table.header = False
table.padding_width = 5
print(table)