names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#dictionary comprehension
import random

student_scores = {student:random.randint(1, 100) for student in names}
# create a new dictionary, with the keys being the students in the names list, and values being a random integer from 1, 100
# print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}

# print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split(" ")}

# print(result)

weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24
}

weather_f = {day:temp * 9 / 5 + 32 for day, temp in weather_c.items()}

print(weather_f)