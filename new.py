import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import folium
from geopy.geocoders import Nominatim

number = input("Enter your number with +__ : ")

phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "en")

print("Phone Number:", number)
print("Time Zones:", list(time))
print("Carrier:", car)
print("Region:", reg)

# Get country name from phone number
country_code = phonenumbers.region_code_for_number(phone)
country_name = geocoder.description_for_number(phone, "en")

# Geocode the country name to retrieve latitude and longitude
geolocator = Nominatim(user_agent="phone-locator")
location = geolocator.geocode(country_name)

if location is not None:
    latitude = location.latitude
    longitude = location.longitude

    # Create a map centered at the location
    map_center = [latitude, longitude]
    m = folium.Map(location=map_center, zoom_start=12)

    # Add a marker for the location
    folium.Marker(
        location=map_center,
        popup=number,
        icon=folium.Icon(color='blue', icon='phone')
    ).add_to(m)

    # Display the map
    m.save('map.html')
else:
    print("Location not found.")
