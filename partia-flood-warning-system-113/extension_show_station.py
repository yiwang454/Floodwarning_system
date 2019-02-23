# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 22:50:53 2018

@author: wangyi66
"""

from floodsystem.stationdata import build_station_list
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d, PanTool, WheelZoomTool)


def run():
    """plot all stations on google map
    """
    #get the stations data 
    stations = build_station_list()
    
    #get the coordinate of the mid points of the most east and west stations
    sort_station_one = sorted(stations, key = lambda station: station.coord[0])
    mid_lat = (sort_station_one[0].coord[0] + sort_station_one[-1].coord[0]) / 2
    
    sort_station_two = sorted(stations, key = lambda station: station.coord[1])
    mid_lng = (sort_station_two[0].coord[1]  + sort_station_two[-1].coord[1]) / 2
    
    #show the map
    map_options = GMapOptions(lat=mid_lat, lng=mid_lng, map_type="roadmap", zoom=6)
    plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
    plot.title.text = "Flood warning"

    plot.api_key = "AIzaSyDu680hgb23BsVmnej1GC5XnALbj0DbjTE" 
    
    #bulid a list of coordinates of the stations 
    #probably need improvement in terms of speed
    
    list_of_lat = []
    list_of_lng = []
    for station in stations:
        list_of_lat.append(station.coord[0])
        list_of_lng.append(station.coord[1])
    
    #plot points on the map
    
    source = ColumnDataSource(
            data= dict(
                    lat = list_of_lat, 
                    lng = list_of_lng,
                    ))
    circle = Circle(x = "lng", y = "lat", size = 5, fill_color = "blue", fill_alpha = 0.8, line_color = None)
    plot.add_glyph(source, circle)
    
    
    plot.add_tools(PanTool(), WheelZoomTool())
    output_file("gmap_plot.html")
    show(plot)

#    for station in stations:
#        print(station.coord[1])
    


if __name__ == "__main__":
    run()
    
    
    
    
    