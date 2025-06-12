import math



# Convert distance to radians (since 1 radian = Earth's radius)
def meters_to_lat(meters):
    # Earth's radius in meters
    R = 6371000 
    return meters / R * (180 / math.pi)

# scale points radious on folium map
def getradius1(ecoli):
    if ecoli<5:
        return 1
    elif ecoli<100:
        return 3
    elif ecoli<300:
        return 6
    else:
        return 10
    
# scale points radious on folium map    
def getradius2(ecoli):
    if ecoli<5:
        return 2
    elif ecoli<10:
        return 3
    elif ecoli<30:
        return 5
    else:
        return 8