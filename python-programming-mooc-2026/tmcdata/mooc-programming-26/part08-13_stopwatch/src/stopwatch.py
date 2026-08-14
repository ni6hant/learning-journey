# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        # if self.seconds<=9:
        #     seconds = "0" + str(self.seconds)
        # else:
        #     seconds = self.seconds
        # if self.minutes<=9:
        #     minutes = "0" + str(self.minutes)
        # else:
        #     minutes = self.minutes
        # return f"{minutes}:{seconds}"
        return f"{self.minutes:02}:{self.seconds:02}"

    def tick(self):
        if self.seconds==59:
            self.minutes+=1
            self.seconds=0
        else:
            self.seconds+=1

        if self.minutes==60:
            self.minutes=0

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(500):
        print(watch)
        watch.tick()