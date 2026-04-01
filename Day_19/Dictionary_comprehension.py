import random
# Syntex of Dictionary_comprehension
# new_dict = {new_key:new_value for item in list}
# Based on the value in an existing dictionary
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# -> {new_key:new_value for (key,value) in dict.items() if test}
names = ["Ali", "Nawaz", "Sahil", "Moon", "Danish", "Suleman"]
student_score = {name:random.randint(1, 100) for name in names}
# passed_student = {key:value for key,value in student_score.items() if value >= 60}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_sentence = sentence.split()
result = {words:len(words) for words in list_sentence}

# Convert celcius to fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
temperature_result = {key:(value * 9/5) + 32 for key, value in weather_c.items()}
print(temperature_result)