import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
#adding elevation values to the python list
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3500:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.748,-79.862], zoom_start=4, tiles='OpenStreetMap')

#adding childer in a different method otherwise you and directly assign the child! 
#Recommended to assign objects seperatly.
fg = folium.FeatureGroup(name="My Map")
#The purpose of zip function is it helps the variables to go together
for lati,longi,el,name in zip(lat,lon,elev,name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    #fg.add_child(folium.Marker(location=[lati,longi],popup=str(el)+" m", icon=folium.Icon(color="darkblue")))
    fg.add_child(folium.CircleMarker(location=[lati,longi],radius=6,popup=folium.Popup(iframe),
                fill_color=color_producer(el), color='grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000<= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
#map.save("Maps_popup.html")   
map.save("Maps_popup_advance.html")  

#fg.add_child(folium.Marker(location=[39.748,-79.862], popup="Let's Go Mountaineers", icon=folium.Icon(color="darkblue")))
#fg.add_child(folium.Marker(location=[40.748,-77.111], popup="Mountainlair", icon=folium.Icon(color="darkblue")))
#map.add_child(fg)
#map.save("Morgantown.html")

