from modules.cli_select import get_location_type, get_user_input
from modules.geocoder import get_custom_location, get_my_location, get_weather, format_weather, combine_weather

def main():
    location_type = get_location_type()

    if (location_type == "My location"):
        [lat, lng], city, country = get_my_location()
        final_message = combine_weather(lat, lng, city, country)
        print(final_message)
    else:
        user_input = get_user_input()
        [lat, lng], city, country = get_custom_location(user_input)

        final_message = combine_weather(lat, lng, city, country)
        print(final_message)


if __name__ == "__main__":
    main()
