inputString = str(input("Word: "))
frameWidth = 30

print("******************************")

countBefore = int((frameWidth- len(inputString) )/2) - 1

if len(inputString)%2 == 0:
    countAfter = countBefore
else:
    countAfter = countBefore+1

print(f'{"*" + " "*countBefore + inputString + " "*countAfter + "*"}')

print("******************************")
