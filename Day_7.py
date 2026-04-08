programming_dictionary = {"Bug": "A moth in your computer",
                          "Function": "A piece of code that you can call easily over and over again.",
                          "Loop": "The action of doing something over and over again"}
# print(programming_dictionary["Bug"])

# Wipe an existing code
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
# print(programming_dictionary["Bug"])

# Loop through dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# Nested List Dictionary
# travel_log = {
#     "Pakistan": ["Sawat", "Gilgit", "Islamabad"],
#     "Germany": ["Stuttgart", "Berlin"]
# }
# print(travel_log["Pakistan"][1])
nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

travel_log = {
    "Pakistan":
    {
        "total visits": 8,
        "cities_visited": ["Sawat", "Gilgit", "Islamabad"]     
    },
     
    "Germany": {
        "total visits": 4,
        "cities_visited": ["Stuttgart", "Berlin", "Hamburg"]
    }
}
pakistan_log = travel_log
print(pakistan_log["Germany"]["cities_visited"][2])