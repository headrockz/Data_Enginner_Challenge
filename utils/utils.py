from math import radians, cos, sin, asin, sqrt
from datetime import *


def distance_miles(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1 
    dlat = lat2 - lat1 

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    miles = (6371 * c) / 1.609

    return miles


def diff_time(arrived_time, departed_time):
    format_time = '%m.%d.%Y %H:%M'
    diff = (datetime.strptime(arrived_time, format_time) - datetime.strptime(departed_time, format_time)).total_seconds()

    return diff / 3600


# Tests
if __name__ == '__main__':
    s = '7.16.2019 7:33'
    t = '7.16.2019 13:02'
    print(diff_time(t, s))

    print(int(distance_miles(-75.948486, 41.054502, -80.837402, 41.112469)))    
