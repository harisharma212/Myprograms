import random

print("welcome to Housy Game: Please press Enter to see First/Next Number\n")

number_list = random.sample(range(1, 91), 90)

notation = {'1': 'st', '2': 'nd', '3': 'rd'}

i = 0

while(i<90):
	data = raw_input("")
	if data == '':
		print('%s%s Number is: %s' % (i+1, notation.get(str(i+1)[-1], 'th'), number_list[i]))
		i += 1
