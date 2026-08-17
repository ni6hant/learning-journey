# write your solution here
student_file = str(input("Student Information: "))
exercise_file = str(input("Exercises completed: "))

names = {}
with open(student_file) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1].strip()+" "+parts[2].strip()

grades = {}
with open(exercise_file) as new_file:
    for line in new_file:
        sumOfGrades=0
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for grade in parts[1:]:
            sumOfGrades+=int(grade)
        grades[parts[0]] = sumOfGrades

for id, name in names.items():
    if id in grades:
        grade = grades[id]
        print(f"{name} {grade}")
    else:
        print(f"{name} 0")
