words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
voyelles = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]

new_list = [
    (word, sum(word.count(voyelle) for voyelle in voyelles)) for word in words
]
print(new_list)
