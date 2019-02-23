"""a cluster of functions related with flood"""
from .station import MonitoringStation
from .stationdata import update_water_levels
from floodsystem.datafetcher import *
from floodsystem.analysis import average_of_latest_level
from .geo import *
from numpy import sqrt  
import matplotlib.pyplot as plt


def stations_level_over_threshold(stations, tol):
    """Returns any input stations that has a latest relative water level above tol
    """
    # update latest water level for each stations
    update_water_levels(stations)

    # filter out under tol stations
    out = []
    for station in stations:
        rel_level = station.relative_water_level()
        if not (rel_level is None) and rel_level > tol:
            out.append(station)
    
    # sort the output data
    out = sorted(out, key=lambda x: x.rel_level, reverse=True)

    return out


def stations_highest_rel_level(stations, N):
    """Returns top N stations of the input stations with regard to their relative water level
    """
    # update latest water level for each stations
    update_water_levels(stations)

    # update station relative water level and filter away stations with no relative water level
    out = []
    for station in stations:
        if not (station.relative_water_level() is None):
            out.append(station)

    # sort stations by relative water level
    out = sorted(out, key=lambda x: x.rel_level, reverse=True)

    return out[:N]


def get_warning_for_town(town):
    """return the warning level for a town name"""

    # grab all stations of the given town name
    stations = stations_by_town(town)

    if len(stations) == 0:
        print('The town does not exist')
        return None

    rel_level_avg = 0
    for station in stations:
        # grab recent few weeks' data for reference
        weeks = 2
        _, recent_data = fetch_recent_data(station.measure_id, weeks)
        if len(recent_data) == 0:
            return None
        try:
            recent_rel_level = sum(recent_data) / float(len(recent_data))
        except:
            print(recent_data)
            raise

        # use a combined average for the current rel_level
        print(station)
        try:
            current_rel_level, _, _ = average_of_latest_level(station, p=3, dt=7, dt_future=2)
        except:
            continue

        # get regulation factor: the temporal local abnormality
        if current_rel_level <= 0:
            reg_factor = 0
        elif recent_rel_level < 0:
            reg_factor = sqrt(current_rel_level / -recent_rel_level)
        else:
            reg_factor = sqrt(current_rel_level / recent_rel_level)

        # get regulated current rel level
        reg_rel_level = reg_factor * current_rel_level

        # get severity
        rel_level_avg += reg_rel_level
    
    rel_level_avg /= float(len(stations))
    print(rel_level_avg)

    if rel_level_avg < 0.75:
        print("town:", town, "has flood severity low")
        return 0
    elif rel_level_avg < 1:
        print("town:", town, "has flood severity moderate")
        return 1
    elif rel_level_avg < 1.25:
        print("town:", town, "has flood severity high")
        return 2
    else:
        print("town:", town, "has flood severity severe")
        return 3