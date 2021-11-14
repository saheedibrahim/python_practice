def lucky_number(name):
  number = len(name) * 9
  result = "Hello " + name + ". Your lucky number is " + str(number)
  return result
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))