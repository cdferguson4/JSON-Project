from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
import plotly
import json

infile = open('eq_data_30_day_m1.json','r')
outfile = open("readable_eq_data.json",'w')

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent=4)

mags,lats,lons,hover_texts =[],[],[],[]

list_of_eqs = eqdata["features"]

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lat = eq["geometry"]["coordinates"][1]
    lon = eq["geometry"]["coordinates"][0]
    title = eq["properties"]["title"]
    lats.append(lat)
    lons.append(lon)
    mags.append(mag)
    hover_texts.append(title)

print(lats[:5])
print(lons[:5])
print(mags[:5])

#data = [Scattergeo(lon=lons,lat=lats)]


data = [{
    'type': 'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_texts,
    'marker':{
        'size':[5*m for m in mags],
        'color':mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title':'Magnitude'}
    }



}]

my_layout = Layout(title="Global Earthquakes One Day ")

fig = {'data': data,'layout':my_layout}

offline.plot(fig, filename= 'globalearthquakes30day.html')