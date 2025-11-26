import math
from datetime import datetime, timedelta

# convert date to required format ayyyyddd for MODIS API calls
def convert_date_to_ayyyyddd(date_str, n_days1, n_days2): 
    # Parse the input date string
    date_obj = datetime.strptime(date_str, "%Y-%m-%d") - timedelta(days=n_days1)
    
    # Add n days to the date
    new_date_obj = datetime.strptime(date_str, "%Y-%m-%d") + timedelta(days=n_days2)

    # Get the year and day of year
    year1 = date_obj.year
    day_of_year1 = date_obj.strftime('%j')  # Julian day
    
    # Get the year and day of year
    year2 = new_date_obj.year
    day_of_year2 = new_date_obj.strftime('%j')  # Julian day
    
    # Format the result
    a_year1 = f"A{year1}"
    a_year_day1 = f"{a_year1}{day_of_year1}"

    # Format the result
    a_year2 = f"A{year2}"
    a_year_day2 = f"{a_year2}{day_of_year2}"
    
    return a_year_day1, a_year_day2


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