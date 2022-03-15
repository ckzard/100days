# =========================INTRO TO PANDAS AND CSV DATA ANALYSIS
# with open("day25/weather_data.csv", "r") as csv_file:
#     weather_data = csv_file.readlines()

# print(weather_data)

# import csv


# with open("day25/weather_data.csv", "r") as csv_file:
#     data = csv.reader(csv_file)

#     temperatures = []
#     temperatures_ints = []

#     for row in data:
#         temperatures.append((row[1]))

#     temperatures.pop(0)

#     for temp in temperatures:
#         temperatures_ints.append(int(temp))

# print(temperatures_ints)

# import pandas

# data = pandas.read_csv("day25/weather_data.csv")

# pandas returns a dataFrame object
# columns are Series objects, and is equivalent to a list basically
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

#getting average
# print(round(sum(temp_list) / len(temp_list)), 1)

#getting average with panda
# print(data["temp"].mean())

# ave_temp = 0
# for temp in temp_list:
#     ave_temp += temp
# print(round(ave_temp / len(temp_list), 1))

# print(data["temp"])
#same as, watch for capitals
# print(data.temp)

#to get a whole row where the day is a monday
# print(data[data.day == "Monday"])

# max_temp = data["temp"].max()

#this will grab a row where the temperature is the max
# print(data[data.temp == data.temp.max()])


#this will grab a row where the day is monay
# monday = data[data.day == "Monday"]
# #and then we can access just the condition value
# print(monday.temp)

# print(monday.temp * 9 / 5 + 32)

#create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }

# data_frame1 = pandas.DataFrame(data_dict)
# data_frame1.to_csv("day25/new_data.csv")
# print(data_frame1)

# ============================================================================================================
# SQUIRREL TIME
import pandas

all_squirrel_data = pandas.read_csv("day25/squirrel_count.csv")

grey_squirrels = all_squirrel_data[all_squirrel_data["Primary Fur Color"] == "Gray"]
red_squirrels = all_squirrel_data[all_squirrel_data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = all_squirrel_data[all_squirrel_data["Primary Fur Color"] == "Black"]

# print("There are", len(grey_squirrels), "gray squirrels")
# print("There are",len(red_squirrels), "red squirrels")
# print("There are", len(black_squirrels), "black squirrels")

squirrel_dict = {
    "Fur Colour" : ["Gray", "Cinnamon", "Black"],
    "Count" : [len(grey_squirrels), len(red_squirrels), len(black_squirrels)]
}

squirrel_colours = pandas.DataFrame(squirrel_dict)

squirrel_colours.to_csv("day25/squir_colours.csv")

