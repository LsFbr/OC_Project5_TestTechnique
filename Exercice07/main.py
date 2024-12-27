# Écrivez votre code ici !
def square(number):
    try:
        result = number * number
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None
    return result


"""
    if not isinstance(number, (int, float)):
        print("Le paramètre doit être un nombre !")
        return None
    return number * number
"""

print(square(5))
