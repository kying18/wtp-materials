# SOLUTION

phrase = input("Enter a phrase: ")
tokens = phrase.split()
acronym = ""
for token in tokens:
    acronym += token[0].upper()

print(f"Your acronym is: {acronym}")
