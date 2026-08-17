# Write your solution here
list= []
nextValue = 0
print(f"The list is now {list}")

while True:
    operation = str(input("a(d)d, (r)emove or e(x)it: "))
    if operation=="x":
        print("Bye!")
        break
    if operation=="d":
        nextValue+=1
        list.append(nextValue)
    if operation=="r":
        list.remove(nextValue)
        nextValue-=1
    print(f"The list is now {list}")