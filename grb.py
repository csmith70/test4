import pygrib
file = 'ds.temp.bin'
gr = pygrib.open(file)
#print inventory
for g in gr:
    print(g)
