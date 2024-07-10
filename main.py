
import pandas
#TODO 1. Create a dictionary in this format:{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
#dict = {key:value for item in list}
dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phoenetic():
    word = input("Enter the word to convert: ").upper()
    try:
        result = [dict[letters] for letters in word]
    except KeyError:
        print("only english letters allowed")
        generate_phoenetic()
    else:
        print(result)
generate_phoenetic()
