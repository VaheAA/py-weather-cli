from modules.cli_select import get_location_type, get_manual_location
from modules.geocoder import get_custom_location, get_my_location, get_weather, format_weather

def main():
    location_type = get_location_type()

    if (location_type == "My location"):
        [lat, lng], city, country = get_my_location()

        weather = get_weather(lat, lng)
        current_weather = weather['current']
        print(format_weather(current_weather, (city, country)))
    else:
        manual_input = get_manual_location()
        location = get_custom_location(manual_input)

        print(location)


if __name__ == "__main__":
    main()
