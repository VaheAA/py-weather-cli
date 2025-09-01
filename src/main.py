from modules.geocoder import get_location, get_weather


def main():
    [lat, lng] = get_location()

    weather = get_weather(lat, lng)
    current_weather = weather['current']
    print(current_weather)


main()
