# Grade: 14 / 15

# Mathias Born
# 2016-05-25
# Homework 2

# 1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
# Display the number of elements in the list

numbers = [22,90,0,-10,3,22,48]
print("Number of numbers:", len(numbers))

# 2) Display the 4th element of this list.

print("Have a look at the forth element of numberful list:", numbers[3])

# 3) Display the sum of the 2nd and 4th element of the list.

print("If I add the forth number of the list to the second, I get", numbers[1] + numbers [3], ".")

# 4) Display the 2nd-largest value in the list.

sortednumbers = sorted(numbers)
print("Tattaa, here's the second largest number of the list:", sortednumbers[len(numbers)-2])

# 5) Display the last element of the original unsorted list.

print("Did you think I messed up my list? Nope, here's the last element of original list:", numbers[len(numbers)-1], ".")

# 6) For each number, display a number:
#if your original number is less than 10, multiply it by thirty.
#If it's also even, add six.
#If it's greater than 50 subtract ten.
#If it's not negative ten, subtract one.
#(For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even,
#so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)

print("Let's do some magic with our numbers. Here's the output. Great, huh?")
for number in numbers:
	if number < 10:
		number1 = number * 30
		if number % 2 == 0:
			number1 = number1 + 6

	if number > 50: # TA-COMMENT: This can be an elif, since < 10 and > 50 won't co-occur (and therefore, the elif will make your code run slightly more efficiently since it won't have to check both conditions)

		number1 = number - 10

	if number != -10:
		number1 = number - 1 # TA-COMMENT: (-1) What if you have already done something to number1? You want to subtract -1 from the most "up-to-date" number, not the original number.

	print("The original number", number, "is now", number1)

# 7) Sum the result of each of the numbers divided by two.

# TA-COMMENT: This looks great!

sum = 0
for number in numbers:
	sum = sum + number / 2
print("Sum of the half of all original numbers:", sum)

# DICTIONARIES
# 8) Sometimes dictionaries are used to describe multiple aspects of a single object.
# Like, say, a movie. Define a dictionary called movie that works with the
# following code.
# print "My favorite movie is", movie['title'], "which was released in",
# movie['year'], "and was directed by", movie['director']

movie = { "title" : "Gold Rush", "year" : 1925, "director" : "Charlie Chaplin"}

# TA-COMMENT: It's probably a good idea to store years as string since we probably won't want to add those together.

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

# 9) Add entries to the movie dictionary for budget and revenue (you'll use code
# like movie['budget'] = 1000), and print out the difference between the two.

print("Movie entry without budget:", movie)
movie["budget"] = 923000
movie["revenue"] = 6500000
print("Movie entry with budget:", movie)
if movie["budget"] > movie["revenue"]:
	print("They lost", movie[budget] - movie[revenue], "dollar.")
elif movie["budget"] - movie["revenue"] == 0:
	print("They didn't win. But they didn't loose either.")
else:
	print("They made", movie["revenue"] - movie["budget"], "dollar.")

# 10) If the movie cost more to make than it made in theaters, print "It was a flop".
# If the film's revenue was more than five times the amount it cost to make,
# print "That was a good investment."

if movie["budget"] > movie["revenue"]:
	print("It was a flop.")
elif movie["revenue"] > movie["budget"] * 5:
	print("That was a good investment. Better than a gold rush.")
else:
	print("They did make some money out of it.")

# 11) Sometimes dictionaries are used to describe the same aspects of many different
# objects. Make ONE dictionary that describes the population of the boroughs of NYC.
# Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m,
# Queens has 2.3m and Staten Island has 470,000.
# (Tip: keeping it all in either millions or thousands is a good idea)

population = { "Manhattan" : 1.6, "Brooklyn" : 2.6, "Bronx" : 1.4, "Queens" : 2.3, "Staten Island" : 0.470 }

# 12) Display the population of Brooklyn.

print("The population of Brooklyn is", population["Brooklyn"], "million.")

# 13) Display the combined population of all five boroughs.

# TA-COMMENT: Yesss, love this structure.

nycpopulation = 0
for borough in population:
	nycpopulation = nycpopulation + population[borough]

# TA-COMMENT: It wouldn't be necessary to make nycpopulation a string if you are consistent with the commas in your print!
print("The population of all boroughs together is", str(nycpopulation) + ".")

#  14) Display what percent of NYC's population lives in Manhattan.

print("About", int(100 * population["Manhattan"] / nycpopulation), "percent of New York's population live in Manhattan.")
