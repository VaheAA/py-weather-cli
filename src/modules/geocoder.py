import geocoder

g = geocoder.ip('me')

def get_location():
    city = g.city
    return city
