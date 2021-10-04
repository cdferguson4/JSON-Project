import json

infile = open('eq_data_30_day_m1.json','r')
outfile = open("readable_eq_data.json",'w')

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent=4)

mags = []
lats = []
lons =[]

list_of_eqs = eqdata["features"]

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lat = eq["geometry"]["coordinates"][1]
    lon = eq["geometry"]["coordinates"][0]
    lats.append(lat)
    lons.append(lon)
    mags.append(mag)

print(lats[:5])
print(lons[:5])
print(mags[:5])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [Scattergeo(lon=lons,lat=lats)]

my_layout = Layout(title="Global Earthquakes One Day ")

fig = {'data': data,'layout':my_layout}

offline.plot(fig, filename= 'globalearthquakes1day.html')