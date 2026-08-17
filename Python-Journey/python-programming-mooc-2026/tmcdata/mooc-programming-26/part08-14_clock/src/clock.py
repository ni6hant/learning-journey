# Write your solution here:
# Write your solution here:
class Clock:
    def __init__(self, hours:int, minutes:int, seconds:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def tick(self):
        # If the time is 23:59:59
        if self.hours==23 and self.minutes==59 and self.seconds==59:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
            return

        # If the seconds are nearing 60 and minutes need to change
        if self.seconds==59:
            #If it's also the end of the hours, increase the hour
            if self.minutes == 59:
                self.hours+=1
                self.minutes = 0
            self.minutes+=1
            self.seconds=0
        else:
            self.seconds+=1

    def set(self,hours:int,minutes:int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)