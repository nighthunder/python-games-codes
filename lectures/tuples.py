geopoints = [(-23.456, 75.344), (14.356,-30.344)] 

for point in geopoints:
    print(point)

print(geopoints[0][0])
print(type(geopoints))
#geopoints[0][0] = -23.789 # TypeError: 'tuple' object does not support item assignment (tuples are immutable)
# You have to convert if you need to change a immutable type
geopoints = [ list(point) for point in geopoints] # list comprehension
geopoints[0][0] = -23.789 
print(geopoints)
geopoints = [tuple(points) for points in geopoints]
print(geopoints)

countries = ("Brazil", "Spain", "France", "Antiqua", "Barbados", "United States", "United Kingdom","Uganda", "Japan")

countries_sorted = tuple(sorted(countries))

for country in countries_sorted:
    print(country)