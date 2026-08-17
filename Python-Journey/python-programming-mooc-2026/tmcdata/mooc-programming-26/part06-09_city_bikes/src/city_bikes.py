# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str):
    aggregated = {}
    with open(filename) as new_file:
        for line in new_file:
            parts = line.strip().split(";")
            if parts[0]=='Longitude':
                continue
            aggregated[parts[3]]=(float(parts[0]),float(parts[1]))
    return aggregated

def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 =  stations[station2][0]
    latitude2 = stations[station2][1]
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    station1 = ""
    station2 = ""
    greatest = 0
    all_stations = []
    for key,value in stations.items():
        all_stations.append(key)
    print(all_stations)
    for i in range(0,len(all_stations)):
        for j in range(i+1,len(all_stations)):
            temp_distance = distance(stations,all_stations[i],all_stations[j])
            if temp_distance > greatest:
                station1 = all_stations[i]
                station2 = all_stations[j]
                greatest = temp_distance
    return (station1, station2, greatest)



if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)