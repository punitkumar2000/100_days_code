import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
"Fur_color" : ["Gray", "Cinnamon", "Black"],
"Count" : [gray_count, cinnamon_count, black_count]
}

data = pandas.DataFrame(data_dict)

data.to_csv("Day25/squirrel_count.csv")