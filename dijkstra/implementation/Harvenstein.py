from math import cos, sin, radians, sqrt, atan2, pi


def harvensineDistance(lat1, lng1, lat2, lng2):
    earthRadius = 3958.7613322984894 # earth's radius in miles
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)
    lng1 = radians(lng1)

    dLat = lat2-lat1;
    dLng = lng2-lng1;
    a = sin(dLat/2) * sin(dLat/2) + cos(lat1) * cos(lat2) * sin(dLng/2) * sin(dLng/2);
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return earthRadius * c


def get_coords(lat,lng):
    return cos(lat) * cos(lng), cos(lat) * sin(lng), sin(lng)

def euclidean_distance(lat1, lng1, lat2, lng2):
    earthRadius = 3958.7613322984894 # earth's radius in miles
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)
    lng1 = radians(lng1)
 

    x = earthRadius * (cos(lat1) * cos(lng1) - cos(lat2) * cos(lng2))
    y = earthRadius * (cos(lat1) * sin(lng1) - cos(lat2) * sin(lng2))
    z = earthRadius * (sin(lat1) - sin(lat2))
    
    return sqrt(x**2 + y**2 + z**2)