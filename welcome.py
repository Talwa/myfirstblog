'''def welcome(Reykjavík):
if city == 'Reykjavík':
	print('Welcome to Reykjavík')
elif name == 'Budapest':
	print('Welcome to Budapest')
else:
	print('Welcome here')
'''

def welcome(city):
	print('Welcome to ' + city)

cities = ['Reykjavík', 'Budapest', 'London', 'Berlin', 'here']
for city in cities:
	welcome(city)
	print('Next city')
