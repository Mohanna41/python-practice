students = {
    'علی': {
        'grades': [18, 15, 20, 19],
        'is_active': True
    },
    'سارا': {
        'grades': [12, 14, 11],
        'is_active': False
    },
    'رضا': {
        'grades': [19, 17, 18, 16],
        'is_active': True
    }
}
for student in students:
    grades = student["grades"]
    total_sum = sum(grades)
    number_of_grades = len(grades)

average = total_sum / number_of_grades
print(f"The average of {student['name']}: {average}")
