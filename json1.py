import json

infile = open('eq_data_1_day_m1.json','r')
outfile = open("readable_eq_data.json",'w')

eqdata = json.load(infile)

json.dump(eqdata,outfile,indent=4)

mags = []
lats = []
lons =[]

list_of_eqs = eqdata["features"]

for eq in list_of_eqs:
    mag = eq["properties"]["mag"]
    lat = eq["geometry"]["coordinates"][0]
    lon = eq["geometry"]["coordinates"][1]
    lats.append(lat)
    lons.append(lon)
    mags.append(mag)

print(lats)
print(lons)
print(mags)