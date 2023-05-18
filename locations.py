from geopy.geocoders import Nominatim


def get_loc_name(latitude, longitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = str(geolocator.geocode(str(latitude) + "," + str(longitude))).split(', ')
    location = f"{location[-1]}, {location[-3]}, {location[1]}, {location[0]}"

    return location
