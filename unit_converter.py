import sys

weig = {'lb': 0.4536, 'mg': .000001, 'kg': 1.0, 'oz': .02835, 'g': .001}
dist = {'ft': 0.3048, 'cm': 0.01, 'mm' : .001, 'mi' : 1609.344,'m': 1.0, 'yd': .9144, 'km': 1000.0, 'in': .0254}
vol = {'L':1.0,'mL':.001,'floz':0.02957,'cup':0.2366,'pint':0.4731,'qt':0.9463,'gal':3.7854}

def error(x):
	"""checks if input is an error"""
	if len(x) != 4:
		return "incorrect num of args"
	try:
		val = float(x[0])
	except ValueError:
		return x[0] + " is not a number"
	if not unit(x[1]):
		return x[1] + " is not a unit of measurement"
	if x[2] != "in":
		return "not valid input format"
	if not unit(x[3]):
		return x[3] + " is not a unit of measurement" 
	if unit(x[1]) != unit(x[3]):
		return x[1] + " and "+ x[3] + " are not in the same category"
	return " "

def unit(x):
	"""checks if what type of measurement x is and returns the dictionary, otherwise it returns false"""
	if dist.has_key(x):
		return dist
	if weig.has_key(x):
		return weig
	if vol.has_key(x):
		return vol
	return False
 
print("Welcome to our Python-powered Unit converter.\n"
	"You can convert Distances , Weights , Volumes & Times to one another\n"
	"within units of the same category, which are shown below.\n"
	"   Distances: ft cm mm mi m yd km in\n"
	"   Weights: lb mg kg oz g\n"
	"   Volumes: floz qt cup mL L gal pint\n")
query = "Convert [AMT SOURCE_UNIT in DEST_UNIT, or (q)uit]:"
input_var = raw_input(query)
while input_var != "q" :
	input = input_var.split()
	errorout = error(input)
	if errorout != " " :
		print(errorout)
		input_var = raw_input(query)
		continue
	scale = float(input[0])
	#finds correct dictionary of dist, weight, or vol
	type = unit(input[1])
	start = type.get(input[1])
	end = 1 / type.get(input[3])
	result = scale * start * end
	print(str(input[0])+" "+str(input[1])+" = "+str(result)+" "+str(input[3]))
	input_var = raw_input(query)
