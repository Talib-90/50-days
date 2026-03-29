import pandas as pd

data = pd.read_csv("Day_17/4. 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
furColor = data["Primary Fur Color"]
furColorList = furColor.tolist()
grayColorCount = furColorList.count("Gray")
# OR
# gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
blackColorCount = furColorList.count("Black")
# OR
# black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamonColorCount = furColorList.count("Cinnamon")
# OR
# cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

squirrel_data_dict = {
    "Fur Color": ["gray", "black", "cinnamon"],
    "Count": [grayColorCount, blackColorCount, cinnamonColorCount]
}
squirrelDataFrame = pd.DataFrame(squirrel_data_dict)
# squirrelDataFrame.to_csv("Day_17/Squirrel Count.csv")