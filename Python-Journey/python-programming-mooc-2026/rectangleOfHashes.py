# Write your solution here

width = int(input("Width: "))
height = int(input("Height: "))
i=0

if width>0 and height>0:
    while i<height:
        print(f'{"#"*width}')
        i+=1
else:
    print("Please input more than 0")

