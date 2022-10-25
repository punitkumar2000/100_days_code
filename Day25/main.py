import pandas

# with open("Day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#----------------------------------
# import csv
# with open("Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for rows in data:
#         if rows[1] != "temp":
#             temperature.append(rows[1])
#     print(temperature)


#----------------------------------
# data = pandas.read_csv("Day25/weather_data.csv")
# print(data["day"] == "Monday")


#-----------------------------------------------------------------------------

import pandas
data = pandas.read_csv("Day25/weather_data.csv")
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)


# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
# or
# print(data["temp"].mean())
# print(data["temp"].max())

#Get data in columns
# print(data["day"])

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

#---------------------------------
#convert c to f

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)


#---------------------------------
# create a dataframe from scratch

data_dict = {
    "students" : ["punit", "mann"],
    "scores" : [90, 95]
}
data = pandas.DataFrame(data_dict)

data.to_csv("Day25/new_csv_file")
