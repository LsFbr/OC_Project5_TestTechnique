words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
voyelles = ["a", "e", "i", "o", "u", "y"]

new_list = [(word, sum(word.count(voyelle) for voyelle in voyelles)) for word in words]
print(new_list)
