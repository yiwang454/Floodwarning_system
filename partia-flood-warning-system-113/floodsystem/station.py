"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d =  "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        '''
        Return True if typical_range[0] <= typical_range[1] or typical_range is None
        '''

        # check typical_range availability
        if self.typical_range is None:
            return False
        
        # check consistency
        return self.typical_range[1] >= self.typical_range[0]

    def relative_water_level(self):
        '''Returns relative latest water level
        if all data are legal
        '''
        # verify data concerned
        if self.latest_level is None or not self.typical_range_consistent():
            return None

        # store data in the object
        self.rel_level = (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])
        
        # return relavtive water level
        return self.rel_level


def inconsistent_typical_range_stations(stations):
    '''This function will apply typical range check to all the input stations
    It will output station names in alphabetical order whose typical range is inconsistent
    '''

    # list comprehension is used here for the reason as follows:
    # for fun dude~
    output = [station.name for station in stations if not station.typical_range_consistent()]

    # sort the output in alphabetical order
    output = sorted(output)

    return output