def grade_points(total_points:int):
    points = total_points
    if points>=0 and points<=14:
        grade = 0
    elif points>=15 and points<=17:
        grade = 1
    elif points>=18 and points<=20:
        grade = 2
    elif points>=21 and points<=23:
        grade = 3
    elif points>=24 and points<=27:
        grade = 4
    elif points>=28:
        grade = 5
    return grade

student_file = str(input("Student Information: "))
exercise_file = str(input("Exercises completed: "))
exam_file = str(input("Exam points: "))

names = {}
with open(student_file) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1].strip()+" "+parts[2].strip()

exercise = {}
with open(exercise_file) as new_file:
    for line in new_file:
        sumOfExercises=0
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for grade in parts[1:]:
            sumOfExercises+=int(grade)
        exercise[parts[0]] = sumOfExercises

exam = {}
with open(exam_file) as new_file:
    for line in new_file:
        sumOfPoints=0
        parts = line.split(';')
        if parts[0] == "id":
            continue
        for points in parts[1:]:
            sumOfPoints+=int(points.strip())
        exam[parts[0]] = sumOfPoints

print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")

for id, name in names.items():
    if id in exercise:
        exercise_points = exercise[id]
        exam_points = exam[id]
        total_points = exam_points+exercise_points//4
        print(f"{name:30}{exercise_points:<10}{exercise_points//4:<10}{exam_points:<10}{total_points:<10}{grade_points(total_points):<10}")
    else:
        print(f"{name} 0")
