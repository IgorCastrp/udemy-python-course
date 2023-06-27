# with open("weather_data.csv", mode="r") as data_file:
#     data = data_file.readlines()
#     print(data)
# import pandas
# import csv
#
# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
#

import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Wednesday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_Fahrenheit = monday_temp * 9/5 + 32
# print(monday_Fahrenheit)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Anderson", "James"],
#     "scores": [79, 58, 77]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
sum_squirrel_gray = sum(data["Primary Fur Color"] == "Gray")
sum_squirrel_red = sum(data["Primary Fur Color"] == "Cinnamon")
sum_squirrel_black = sum(data["Primary Fur Color"] == "Black")

squirrel_data_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [sum_squirrel_gray, sum_squirrel_red, sum_squirrel_black]
}

squirrel_count = pd.DataFrame(squirrel_data_dict)
squirrel_count.to_csv("squirrel_count.csv")
