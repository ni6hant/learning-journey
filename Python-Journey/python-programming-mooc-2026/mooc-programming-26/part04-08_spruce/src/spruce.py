# Write your solution here
# You can test your function by calling it within the following block

def spruceLine(level,height):
    print(" "*(height-level)+"*"*(1+2*(level-1))+" "*(height-level))

def triangularPattern(spruceHeight):
    count = 0
    while count<spruceHeight:
        spruceLine(count+1,spruceHeight)
        count+=1

def spruce(spruceHeight):
    print("a spruce!")
    triangularPattern(spruceHeight)
    spruceLine(1,spruceHeight)
 

if __name__ == "__main__":
    
    spruce(3)