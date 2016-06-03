# Mathias Born
# May 23, 2016
# Homework 1

import time
yearofbirth = input("What year were you born in? ")
if int(yearofbirth) < 1900 or int(yearofbirth) > 2016:
	print("You are kidding me. Think -- and try again.")
	yearofbirth = input("What year were you born in? ")
	if int(yearofbirth) < 1900 or int(yearofbirth) > 2016:
	        print("Really. Well, wonders happen. I trust you this time. Let's go on.")
age = 2016 - int(yearofbirth)
yearminutes = 60 * 24 * 365.2424
heartbeat = yearminutes * 72 * age # Heartbeat according to http://www.cardio-research.com/quick-facts/animals
whale = yearminutes * 6 * age # Heartbeat according to http://www.cardio-research.com/quick-facts/animals
rabbit = yearminutes * 205 * age # Heartbeat according to http://www.cardio-research.com/quick-facts/animals
venus = 365.2424 / 225 * age
neptun = 365.2424 / 165 * age
developersage = 40
steelers = [1975,1976,1979,1980,2006,2009] # Years the Pittsburgh Steelers won the Superbowl accoring to own memory. (Just kidding. According to http://www.steelers.com/history/superbowl.html.)
presidents = {"Franklin D. Roosevelt" : 1933, "Harry S Truman" : 1945, "Dwight D. Eisenhower" : 1953, "John F. Kennedy" : 1961, "Lyndon B. Johnson" : 1963, "Richard Nixon" : 1969, "Gerald Ford" : 1974, "Jimmy Carter" : 1977, "Ronald Reagan" : 1981, "George Bush" : 1989, "Bill Clinton" : 1993, "George W. Bush" : 2001, "Barack Obama" : 2009}

print("\n")
print("Well buddy, let's do some math. You are approximately", int(age), "years old.")
time.sleep(2) 
print("\n")
print("Your heart has beaten about", int(heartbeat), "times.")
time.sleep(2) 
print("A blue whale's heart has beaten in the same period about", int(whale), "times.")
time.sleep(2) 
if rabbit > 1000000000:
	print("A rabbit's heart has beaten about", int(rabbit / 1000000000), "billion times.")
else:
	print("A rabbit's heart has beaten about", int(rabbit), "times.")
print("\n")
time.sleep(2) 
print("On Venus you would be", int(venus), "years old. Kinda feeling like grandpa now?")
time.sleep(3) 
print("On Neptun you would be", int(neptun), "years old. Feels like great grandfather, huh?")
print("\n")
time.sleep(4) 
if developersage - age > 0: 
	print("By the way: You are ", developersage - age, "year(s) younger than the developer of the amazing software that you are currently running. Darn it.")
elif developersage - age == 0:
	print("You are more or less the same age as the developer of this program. It'a beautiful age, isn't it?")
else:
	print("You are", abs(developersage - age), "year(s) older than the young bung who wrote this great software product. But you still look pretty crispy.")
time.sleep(3)
if int(yearofbirth) % 2 == 0:
	print("You were even born in an even year.")
else: 
	print("You were born in an uneven year.")
print("\n")
time.sleep(3) 

# Pittsburgh saga
supercounter = 0
for i in range(int(yearofbirth),2016,1):
	if i in steelers:
		supercounter +=1

print("Let's dive deeply into history. During the time of your life the Pittsburgh Steelers won", supercounter, "times the superbowl. But you didn't. Not a single time.")
time.sleep(4) 

# The presidents
if int(yearofbirth) >= 2009:
	print("President Barack Obama was in charge when you were born.")
elif int(yearofbirth) >= 2001:
	print("President George W. Bush was in charge when you were born.")
elif int(yearofbirth) >= 1993:
        print("President Bill Clinton was in charge when you were born.")
elif int(yearofbirth) >= 1989:
        print("President George Bush was in charge when you were born.")
elif int(yearofbirth) >= 1981:
        print("President Ronald Reagan was in charge when you were born.")
elif int(yearofbirth) >= 1977:
        print("President Jimmy Carter was in charge when you were born.")
elif int(yearofbirth) >= 1974:
        print("President Gerald Ford was in charge when you were born.")
elif int(yearofbirth) >= 1969:
        print("President Richard Nixon was in charge when you were born.")
elif int(yearofbirth) >= 1963:
        print("President Lyndon B. Johnson was in charge when you were born.")
elif int(yearofbirth) >= 1961:
        print("President John F. Kennedy was in charge when you were born.")
elif int(yearofbirth) >= 1953:
        print("President Dwight D. Eisenhower was in charge when you were born.")
elif int(yearofbirth) >= 1945:
        print("President Harry S Truman was in charge when you were born.")
elif int(yearofbirth) >= 1933:
        print("President Franklin D. Roosevelt was in charge when you were born.")
else: 
	print("You are sooo old? Well, I have to look for a history book to find the matching president...")
time.sleep(2) 

for key, value in presidents.items() : 
	if int(yearofbirth) <= value :
		#print ("President", key[key-1], "was in charge.")
		print ("You also survived president", key, "( inauguration:", value, ").")
		time.sleep(1) 

