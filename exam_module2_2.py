#Implement below:

def format_name(first_name, last_name):
	# code goes here
	if first_name == "" or last_name == "":
		return "Name: " + first_name + " " + last_name
	else:
		return "Name: " + first_name + " " + last_name
	
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string