from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list


def run():
    """testing for stations_highest_rel_level
    """

    # generate stations list
    stations = build_station_list()

    # output the top 10 stations with regard to their rel_level
    output = stations_highest_rel_level(stations, 10)

    # print with format: name, relative level
    for station in output:
        print(station.name, station.rel_level)


if __name__ == "__main__":
    run()