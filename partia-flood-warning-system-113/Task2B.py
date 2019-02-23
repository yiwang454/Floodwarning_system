from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list


def run():
    """testing for station_level_over_threshold
    """

    # generate stations list
    stations = build_station_list()

    # output station with relative water level above 0.8
    output = stations_level_over_threshold(stations, 0.8)

    # print with format: name, relative level
    for station in output:
        print(station.name, station.rel_level)


if __name__ == "__main__":
    run()