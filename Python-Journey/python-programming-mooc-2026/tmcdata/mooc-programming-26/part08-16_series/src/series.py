# Write your solution here:
class Series:
    def __init__(self,title:str,seasons:int,genre:[]):
        self.title = title
        self.seasons = seasons
        self.genre = genre
        self.ratings = []
        self.average_rating = 0.0

    def __str__(self):
        printString = f"{self.title} ({self.seasons} seasons)"
        printString += "\n"
        printString += f"genres: {", ".join(self.genre)}"
        printString += "\n"
        if len(self.ratings)==0:
            printString += "no ratings"
        else:
            ratingsCount = len(self.ratings)
            ratingsSum = sum(self.ratings)
            ratingsAverage = ratingsSum/ratingsCount
            printString += f"{ratingsCount} ratings, average {ratingsAverage:0.1f} points"
        return printString

    def rate(self, rating:int):
        if rating<0 or rating >5:
            raise ValueError("Ratings should be between 0 and 5 only")
        else:
            self.ratings.append(rating)
            ratingsCount = len(self.ratings)
            ratingsSum = sum(self.ratings)
            ratingsAverage = ratingsSum/ratingsCount
            self.average_rating = ratingsAverage


def minimum_grade(rating: float, series_list: list):
    minimum_grade_list = []
    for series in series_list:
        if series.average_rating>rating:
            minimum_grade_list.append(series)
    return minimum_grade_list

def includes_genre(genre:str, series_list:list):
    includes_genre_list = []
    for series in series_list:
        if genre in series.genre:
            includes_genre_list.append(series)
    return includes_genre_list

# if __name__ == "__main__"

#     s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
#     s1.rate(5)

#     s2 = Series("South Park", 24, ["Animation", "Comedy"])
#     s2.rate(3)

#     s3 = Series("Friends", 10, ["Romance", "Comedy"])
#     s3.rate(2)

#     series_list = [s1, s2, s3]

#     print("a minimum grade of 4.5:")
#     for series in minimum_grade(4.5, series_list):
#         print(series.title)

#     print("genre Comedy:")
#     for series in includes_genre("Comedy", series_list):
#         print(series.title)