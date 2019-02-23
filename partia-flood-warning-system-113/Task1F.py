from floodsystem.stationdata import build_station_list
from floodsystem import station

def run():
    '''Testing for inconsistent_typical_range_stations
    '''

    # generate stations list
    stations = build_station_list()

    # get consistent station names
    output = station.inconsistent_typical_range_stations(stations)

    print(output)
    return output


if __name__ == "__main__":
    a = station.MonitoringStation(0, 0, 0, 0, (1, 1), 0, 0)
    run()