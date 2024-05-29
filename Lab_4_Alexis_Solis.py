import folium

from folium.plugins import minimap

popuptext = '<b>Guanacaste</b>'

my_map = folium.Map(location=(9.999178834501198, -84.11152339466842))
folium.Marker(location=[9.999178834501198, -84.11152339466842], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[9.999178834501198, -84.11152339466842],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map1 = folium.Map(location=(9.971025180176563, -84.12838362384284))
folium.Marker(location=[9.971025180176563, -84.12838362384284], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[9.971025180176563, -84.12838362384284],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map2 = folium.Map(location=(10.019955728789132, -84.19699314626158))
folium.Marker(location=[10.019955728789132, -84.19699314626158], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[10.019955728789132, -84.19699314626158],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map3 = folium.Map(location=(10.319318906356644, -83.92274707509426))
folium.Marker(location=[10.319318906356644, -83.92274707509426], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[10.319318906356644, -83.92274707509426],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map4 = folium.Map(location=(8.573546039505455, -82.87244535395028))
folium.Marker(location=[8.573546039505455, -82.87244535395028], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[8.573546039505455, -82.87244535395028],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map5 = folium.Map(location=(9.400712207736126, -83.69127669815522))
folium.Marker(location=[9.400712207736126, -83.69127669815522], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[9.400712207736126, -83.69127669815522],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map6 = folium.Map(location=(10.617770463276464, -85.45132144441304))
folium.Marker(location=[10.617770463276464, -85.45132144441304], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[10.617770463276464, -85.45132144441304],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

my_map7 = folium.Map(location=(10.134809054227658, -85.44663775385258))
folium.Marker(location=[10.134809054227658, -85.44663775385258], popup=popuptext,icon=folium.Icon(color="orange",icon="ok-sign")).add_to(my_map)
folium.Circle(location=[10.134809054227658, -85.44663775385258],color="purple",weight=6,fill_color="red",fill_opacity=0.5,tooltip="Guanacaste").add_to(my_map)

minimap = minimap.MiniMap(title_layer='statementerrain', position='bottomright')

my_map.add_child(minimap)