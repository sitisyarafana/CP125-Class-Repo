def find_station(stations, name):
    
    for i in range(len(stations)):
        if stations[i] == name:
            return i

    return -1
         

def count_stops(stations, start, stop): 
    stations_start = find_station(stations, start)
    stations_stop = find_station(stations, stop)

    if stations_start == -1 or stations_stop == -1:
        return -1
    
    distance = stations_start - stations_stop

    if distance < 0:
        return distance * -1

    return distance