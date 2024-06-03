

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#dict = {key:value for item in list}
dict = {row.letter:row.code for (index, row) in data.iterrows()}
#print(dict)

name = input("Enter the word to convert: ").upper()
result = [dict[letters] for letters in name]
print(result)
