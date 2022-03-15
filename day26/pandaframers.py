#Iterate over panda dataframes

student_dict = {
    "student" : ["Angela", "Chris", "Lily"],
    "score": [56, 76, 98]
}

#loop through the dictionary
for key, value in student_dict.items():
    # print(value)
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#loop through data from using vanilla python
for key, value in student_data_frame.items():
    # print(value)
    pass

# or iterate through using panddas method iterrows()
for (index, row) in student_data_frame.iterrows():
    print(row.student, row.score)
    #each row is a pandas series object, so you can access the attributes of each object using dot notation

#dictionary comprehension, iterrows through data frame to make a new dictionary
new_dict = {row.student: row.score for (index, row) in student_data_frame.iterrows()}
print(new_dict)