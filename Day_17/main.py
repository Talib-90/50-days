# with open("Day_17/weather_data.csv", "r") as dataFile:
#     data = dataFile.readlines()
#     print(data)
# dataFile.close()

# import csv
# with open("Day_17/weather_data.csv", "r") as dataFile:
#     data = csv.reader(dataFile)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

# print(temperature)
"""The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional), 
    handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering."""
import pandas
data = pandas.read_csv("Day_17/weather_data.csv")
# print(data)
# print(data["temp"])
# Dataframes converted to dictionary
data_dict = data.to_dict()
# print(data_dict)

# print(data["temp"].tolist())

# Calculate temp average
# average = sum(temp_list) / len(temp_list)
# print(round(average,2))

# OR using series method 
# print(data["temp"].mean())

# Maximum number
# print(data["temp"].max())

# Get data in columns
# print(data["condition"]) 
# OR
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# temp_monday = monday["temp"].tolist()[0]
# fehrenheit = (temp_monday * 9/5) + 32 
# print(fehrenheit)

# Create dataframe from scratch
data_student = {
    "student" : ["Ali", "Nawaz", "Siraj"],
    "scores": [56, 63, 72]
}
createDataFrame = pandas.DataFrame(data_student)
createDataFrame.to_csv("Day_17/new_csv.csv")