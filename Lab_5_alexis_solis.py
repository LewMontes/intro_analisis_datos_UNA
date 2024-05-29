from geopy.distance import geodesic
from google.colab import files
import folium

lat, lon=9.7489,-83.7534
lat1, lon1=35.36240815942667, 138.7277923237685
distance = geodesic((lat,lon),(lat1,lon1))
print(f"La distancia entre las 2 ubicaciones es de {distance}")

monte_fuyi = folium.Map(location = [lat1,lon1],zoom_start = 7)
monte_fuyi.save("monte.html")
files.download("monte.html")

monte_fuyi