# Write your solution here
def getInput():
    pointsList = []
    exercisesList = []
    while True:
        combinedData = str(input("Exam points and exercises completed: "))
        if combinedData == "":
            break
        else:
            temp = ""
            for char in combinedData:
                if char !=  " ":
                    temp = temp+char
                else:
                    points = int(temp)
                    temp=""
            exercises =int(temp)//10
            pointsList.append(points)
            exercisesList.append(exercises)
    return (pointsList,exercisesList)

def gradeDistributionPrint(result:list):
    i=len(result)-1
    while i>=0:
        print(f'  {i}: {result[i]*"*"}')
        i-=1
    return

def gradeSystem():
    input = getInput()
    pointsList = input[0]
    exercisesList = input[1]
    #count of total students is stored as this
    # fail, 1, 2, 3, 4, 5
    #  totalPoints <=14, 15<= totalPoints <=17, 18<= totalPoints <=20, 21<= totalPoints <=23 , 24<= totalPoints <=27 ,  28<= totalPoints <=30
    result = [0,0,0,0,0,0]
    i = 0
    grandTotal = 0
    while i<len(pointsList):
        examPoints = pointsList[i]
        exercisePoints = exercisesList[i]
        totalPoints=examPoints+exercisePoints
        grandTotal += totalPoints
        if totalPoints<=14 or examPoints<10:
            result[0]+=1
        elif 15<= totalPoints <=17:
            result[1]+=1
        elif 18<= totalPoints <=20:
            result[2]+=1
        elif 21<= totalPoints <=23:
            result[3]+=1
        elif 24<= totalPoints <=27:
            result[4]+=1
        elif 28<= totalPoints <=30:
            result[5]+=1
        i+=1
    passPercentage = (sum(result)-result[0])/(len(pointsList))*100
    print("Statistics:")
    print(f"Points average: {grandTotal/len(pointsList):.1f}")
    print(f"Pass percentage: {passPercentage:.1f}")
    print("Grade distribution:")
    gradeDistributionPrint(result)

gradeSystem()