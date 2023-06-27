# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
from prettytable import PrettyTable, DOUBLE_BORDER
from prettytable.colortable import ColorTable, Themes

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.shapesize(2, 2, 4)
# timmy.forward(100)
# timmy.color("purple1", "yellow")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


table = ColorTable(theme=Themes.OCEAN)
table_2 = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align, "\n\n")


table.align = "l"
table.align["Type"] = "r"
table_2.align = "r"


# table.set_style(DOUBLE_BORDER)


table_2.field_names = ["Pokemon Name", "Type"]
table_2.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ],

)

print(table, "\n\n")
print(table_2.get_string(fields=["Type"]))
