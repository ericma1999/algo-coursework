from math import sqrt

def euclidean_distance(lat1, lng1, lat2, lng2):
    return sqrt((lat1-lat2) ** 2 + (lng1-lng2) ** 2)