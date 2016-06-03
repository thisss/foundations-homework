# Mathias Born
# May 30 2016
# Homework 3

# LISTS
# 1) Make a list called "countries" - it should contain seven different countries 
# and NOT be in alphabetical order.
countries = [ "Switzerland", "France", "Italia", "Poland", "USA", "China", "Peru"]

# 2) Using a for loop, print each element of the list
for country in countries: 
	print(country)

# 3) Sort the list permanently.
countries.sort()

# 4) Display the first element of the list
print(countries[0])

# 5) Display the second-to-last element of the list using a line of code that 
# will work no matter what the size of the list is (hint: len will be helpful).
print(countries[len(countries)-2])

# 6) Delete one of the countries from the list using its name 
# (we didn't learn this in class).
del countries[3]

# 7) Using a for loop, print each element of the list again, which should now be 
# one element shorter.
for country in countries:
	print(country)

#DICTIONARIES
# These will require LATITUDE and LONGITUDE. You can ask Google for latitude 
# and longitude by typing in *coordinates of CITYNAME*. 
# You can also use http://itouchmap.com/latlong.html. Store the latitude 
# and longitude without the N/S/E/W - if the latitude is S, make it negative. 
# If the longitude is W, make it negative. See here for explanation: 
# https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8

# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 
# 'location_name', 'latitude' and 'longitude'. Pick a tree from here: 
# https://en.wikipedia.org/wiki/List_of_trees
tree = { "name" : "Alishan Sacred Tree", "species" : "Cypress", "age" : 3000, "location_name" : "Alishan", "latitude" : 23.5166646, "longitude" : 120.7999968 }

# 2) Print the sentence "{name} is a {years old} tree that is in {location_name}."
print("The", tree["name"], "is a", tree["age"], "years old tree that is in", tree["location_name"] + ".")

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see 
# if the tree is south of NYC, and print "The tree {name} in {location} is south 
# of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
ny = {"name" : "New York City", "latitude" : 40.7128, "longitude" : 74.0059 }
if ny["latitude"] > tree["latitude"]:
	print("The", tree["name"], "in", tree["location_name"], "is south of NYC.")
elif ny["latitude"] < tree["latitude"]:
	print("The", tree["name"], "in", tree["location_name"], "is south of NYC.")
else:
	print("The tree is standing on the exact same latitude than NY is located. Maybe it is... in New York?")

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." 
# If they are younger than the tree, display "{name} was {XXX} years old when you were born."
userage = int(input("How old are you? "))
if userage > tree["age"]:
	print("You are kidding me -- you are really", userage - tree["age"], "older than the", tree["name"] + "?")
elif userage < tree["age"]:
	print("The", tree["name"], "was", tree["age"] - userage, "years old when you were born.")
else:
	print("The", tree["name"], "has exactly the same age as you. Maybe you should party together.")

#LISTS OF DICTIONARIES
# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago. 
# Each dictionary should include each city's name and latitude/longitude (see note above).
cities = [
	{"name" : "Moscow", "latitude" : 55.751244, "longitude" : 37.618423 },
	{"name" : "Tehran", "latitude" : 35.715298, "longitude" : 51.404343 },
	{"name" : "Falkland Islands", "latitude" : -52.094273, "longitude" : -60.833874 },
	{"name" : "Seoul", "latitude" : 37.532600, "longitude" : 127.024612 },
	{"name" : "Santiago", "latitude" : -33.447487, "longitude" : -70.673676 }
]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). 
# When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," 
# which is a sentence I stole from Wikipedia.

for city in cities: 
	if city["latitude"] > 0:
		print(city["name"], "is above the equator.")
	elif city["latitude"] < 0:
		if city["name"] == "Falkland Islands":
			print("The", city["name"], "are below the equator. By the way: The Falkland Islands are a biogeographical part of the mild Antarctic zone.")
		else:
			print(city["name"], "is below the equator.")
	else:
		print(city["name"], "is one of the rare cities exactly located on the equator. You have to memorize that, dude.")

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.

for city in cities:
	if city["latitude"] > tree["latitude"]:
		print(city["name"], "is north of the famous", tree["name"] + ".")
	elif city["latitude"] < tree["latitude"]:
		if city["name"] == "Falkland Islands": 
			print("The", city["name"], "are south of the famous", tree["name"] + ". By the way: Did we already mention that the Falkland Islands are a biogeographical part of the mild Antarctic zone?")
		else:
			print(city["name"], "is south of the famous", tree["name"] + ".")
	else:
		print(city["name"], "is exactly on the same latitude than our beloved", tree["name"])

print("\n")
print("Please memorize these random facts! They might serve to impress someone at the next party. Especially the fact that the Falkland Islands are a biogeographical part of the mild Antarctic zone.")
