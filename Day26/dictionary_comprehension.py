# new_dict = {new_key : new_value for (key,value) in dict.items()}
# import random
# names = ["punit", "mann", "neha", "python"]

# new_dict = {student: random.randint(1, 100) for student in names}
# print(new_dict)


# passes = {student : score for (student,score) in new_dict.items() if score < 50}
# print(passes)

student_dict = {
"student": ["punit", "mann"],
"score": [50, 60]
}

# for (key,value) in student_dict.items():
#     print(value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#loop through a data frame
# for (key,value) in student_data_frame.items():
#     print(key)

#loop through rows of data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "mann":
        print(row)