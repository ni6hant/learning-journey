# Write your solution here
from datetime import datetime as dt

def is_it_valid(pic:str):
    # d d m m y y X y y y z
    # 0 1 2 3 4 5 6 7 8 9 10
    
    if len(pic)!=11:
        return False
    
    centuryMarker = pic[6]
    if centuryMarker =="+":
        year = 1800
    elif centuryMarker =="-":
        year = 1900
    elif centuryMarker =="A":
        year = 2000
    else:
        return False

    date_string = pic[:4]
    day = int(pic[0:2])
    month = int(pic[2:4])
    year += int(pic[4:6])

    try:
        dt(year,month,day)
    except:
        return False
    
    control_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    control_character = control_string[int("".join([pic[0:6],pic[7:10]]))%31]

    if control_character != pic[10]:
        return False

    return True

if __name__ == "__main__":
    print(is_it_valid("081142-720N"))