# Write your solution here
# def longest_series_of_neighbours(myList:list):
#     newList=[]
#     tempList=[]
#     i=1
#     while i<=len(myList)-1:
#         if myList[i]-myList[i-1] == 1 or myList[i]-myList[i-1]==-1:
#             tempList.append(myList[i-1])
#             tempList.append(myList[i])
#             if len(newList)<len(tempList):
#                 newList=tempList
#         else:
#             # tempList.append(myList[i-1])
#             if len(newList)<len(tempList):
#                 newList=tempList
#             tempList=[]
#         i+=1
#     return newList

def longest_series_of_neighbours(myList:list):
    maximum_length = 0
    temp=1
    i=0
    while i<len(myList)-1:
        if myList[i+1]:
            if myList[i+1]-myList[i] == 1 or myList[i+1]-myList[i]==-1:
                temp+=1
            else:
                temp=1
        else:
            temp=1
        if temp>maximum_length:
            maximum_length=temp
        i+=1
    return maximum_length

if __name__ == "__main__":
    longest_series_of_neighbours([1, 2, 3, 0, 1, 2, 3, 4, 5, 3, 4, 5, 1, 2, 3])