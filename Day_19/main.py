import pandas

student_dict = {
    "student": ["Ali", "Wahaj", "Nadir", "Shahid", "Farhan"],
    "score": [59, 78, 54, 89, 98]
}

# for (key, value) in student_dict.items():
#     print(key)

student_dict_dataframe = pandas.DataFrame(student_dict)
# print(student_dict_dataframe)

# Loop through dataframe
for (key, value) in student_dict_dataframe.items():
    print(value)

    
# Loop through rows of dataframe
for (index, row) in student_dict_dataframe.iterrows():
    # print(row.student)
    if row.student == "Wahaj":
        print(f"Name: {row.student}, Score: {row.score}")

