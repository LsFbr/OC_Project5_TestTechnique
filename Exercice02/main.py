students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
    'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
}

# Demande du nom de l'étudiant
student_name = input("Entrez le nom de l'étudiant : ")

# Vérification si l'étudiant existe
if student_name in students:
    # Affichage des notes de l'étudiant
    print(f"Notes de {student_name} :")
    total_grades = 0
    for course, grade in students[student_name].items():
        print(f"{course} : {grade}")
        total_grades += grade

    # Calcul et affichage de la moyenne des notes
    average_grade = total_grades / len(students[student_name])
    print(f"Moyenne de {student_name} : {average_grade}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
