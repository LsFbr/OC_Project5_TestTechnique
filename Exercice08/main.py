def log_decorator(func):
    def wrapper():
        print("Début de la fonction")
        func()
        print("Fin de la fonction")
    return wrapper


@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")


function_test()
