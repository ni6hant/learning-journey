# Write your solution here

def add_student(students:dict,name:str):
    if name not in students:
        students[name] = []

def add_course(students:dict, name:str, course_data:tuple):
    if name not in students:
        print(f"{name} doesn't exist in database as a student")
        return
    flag = True
    # for course in students[name]:
    #     if course_data[0] in course[0]:
    #         flag = False
    #         if course_data[1]>course[1]:
    #             course=course_data
    for i in range(0,len(students[name])):
        if course_data[0]==students[name][i][0]:
            flag = False
            if course_data[1]>students[name][i][1]:
                del students[name][i]
                students[name].append(course_data)
    if flag and course_data[1]!=0:
        students[name].append(course_data)

def print_student(students, name:str):
    if name not in students:
        print(f"{name}: no such person in the database")
        return
    
    print(f"{name}:") #print Name
    
    if students[name] == []:
        print(" no completed courses")
    else:
        print(f" {len(students[name])} completed courses:")
        sum_grade = 0
        for course in students[name]:
            print(f"  {course[0]} {course[1]}")
            sum_grade+=course[1]
        print(f" average grade {sum_grade/len(students[name]):.1f}")

def average_grade():
    return 

def summary(students:dict):
    print(f"students {len(students)}")
    most_courses = 0
    best_average_grade = 0
    
    for student in students:

        if len(students[student])>most_courses:
            most_courses = len(students[student])
            most_courses_student = student
        
        sum_grade = 0
        for course in students[student]:
            sum_grade+=course[1]
        average_grade_temp = sum_grade/len(students[student])
        if average_grade_temp > best_average_grade:
            best_average_grade = average_grade_temp
            best_average_grade_student = student

    print(f"most courses completed {most_courses} {most_courses_student}")
    print(f"best average grade {best_average_grade} {best_average_grade_student}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)