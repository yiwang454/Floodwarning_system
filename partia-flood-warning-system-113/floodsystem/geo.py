"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key

from floodsystem.haversine import haversine as hs
from floodsystem.stationdata import build_station_list


def stations_by_distance(stations, p):
    '''
    This function will output a list of (station, distance) of the disctance of input stations and given destination p
    input variables:
            stations:     list: a list of MonitoringStation objects
            p:            tuple: the coord we compare to
    '''
    output = []

    # collect all the (station, distance) tuples
    for station in stations:
        distance = hs(station.coord, p)
        output.append((station, distance))

    # sort the output tuples with respect to distance
    output = sorted_by_key(output, 1)

    return output


def stations_within_radius(stations, center, r):
    '''
    This function will return a list of stations(type MonitoringStation)
    input: 
        stations : a list of MonitoringStation objects, 
        center:  coordinate of x
        r : the radius
    '''
    new_stations = []
    for station in stations:
        distance = hs(station.coord, center)
        if distance < r:
            new_stations.append(station)
            
    return new_stations
            

def rivers_with_stations(stations):
    '''
    This function returns a set of the name of rivers having at least one station
    Input :
        stations:      a list of MonitoringStation objects
    '''
    #get the name of rivers with stations
    rivers = set()
    for station in stations:
        rivers.add(station.river)
        
    return rivers
        
def stations_by_river(stations):
    '''
    This function returns a dictionary that map river names to a list of station objects on the river.
    Input :
        stations:      a list of MonitoringStation objects
    '''
    
    rivers_with_st = dict()
    
    for river in rivers_with_stations(stations):
        list_of_st = []
        
        for station in stations:
            #forming a list with stations of that river
            if station.river == river:
                list_of_st.append(station.name)
        #adding the list into map
        rivers_with_st[river] = list_of_st
        
    return rivers_with_st


def rivers_by_station_number(stations, N):
    '''
    This function returns a list of tuples (river name, number of stations on that river)
    The list only includes N rivers with the greatest number of monitoring stations
    input : stations:      a list of MonitoringStation objects
            N              an int 
    '''
    
    # Get a list of tuples of all rivers ( river name, number of stations )
    list_of_tuple = []
    map_with_stations = stations_by_river(stations)
    set_of_river = rivers_with_stations(stations)
    
    for river in set_of_river:
        specific_list = map_with_stations[river]
        num = len(specific_list)
        list_of_tuple.append((river, num))
        
    # sorted by numbers  (from small to large)
    sorted_rivers = sorted(list_of_tuple, key=lambda tup: (-tup[1], tup[0]), reverse=False)
    
    # tell the number of stations of the lastest N station
    num_of_Nth = sorted_rivers[N-1][1]
    
    # list : the river with number of stations larger that N
    final_list = []
    for river in sorted_rivers:
        if river[1] >= num_of_Nth:
            final_list.append(river)
            
    return final_list


def stations_by_town(town):
    """get stations of a given town name"""

    assert type(town) is str

    #get the stations data and sorted by latest water level
    stations = build_station_list()

    output = []
    for station in stations:
        if station.town == town:
            output.append(station)
        
    return output
    
    
    
