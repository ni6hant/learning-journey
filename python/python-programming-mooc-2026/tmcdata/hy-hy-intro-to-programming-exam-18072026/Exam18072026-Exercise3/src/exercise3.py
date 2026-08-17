def read_points():
    read_points_list=[]
    
    with open("statistics.txt") as new_file:
        for line in new_file:
            line = line.replace("\n", "")

            # [team]:[wins]-[losses]-[ties]
            parts = line.split(":")
            points_list = parts[1].split("-")
            # three points for a win, one point for a tie, and no points for a loss.
            try:
                wins = int(points_list[0])
                losses = int(points_list[1])
                ties = int(points_list[2])
            except ValueError:
                raise ValueError(f"Invalid format in the file: {line}")

            points = wins*3 + ties*1
            read_points_list.append((parts[0],points))

    return read_points_list
    # returns a list of tuples. [(team_name, points),...]

if __name__ == "__main__":
    print(read_points())