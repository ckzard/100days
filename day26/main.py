#use pandas read csv to create a datafram to iterate through
import pandas
nato_df = pandas.read_csv("day26/nato_phonetic_alphabet.csv")
# print(nato_df)

# create a dictionary, key is the letter, value is the code
#dict comprehension
nato_dict = {row.letter : row.code for (index, row) in nato_df.iterrows()}
# print(nato_dict)

#normal lopp
# nato_dict2 = {}
# for index, row in nato_df.iterrows():
#     nato_dict2[row.letter] = row.code

name_input = input("Enter a word: ").upper()
name_input_split = [letter.upper() for letter in name_input]


#creata  list of the phonetic code words that the user inputs.
#list comprehension
nato_words_list2 = [nato_dict[letter] for letter in name_input]
nato_words_list = [word for (key, word) in nato_dict.items()]
# print(nato_words_list)
print(nato_words_list2)

#normal loop
# nato_words_list2 = []
# for key, value in nato_dict.items():
#     nato_words_list2.append(value)

#split the name inputted into individual letters

# word_codes = []
#normal loop
# for letter in name_input_split:
#     for code in nato_words_list:
#         if letter == code[0]:
#             word_codes.append(code)

#list comp

# print(word_codes)



