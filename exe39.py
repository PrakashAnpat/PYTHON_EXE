states = {'Oregon':'OR','Florida':'FL','California':'CA','New York':'NY','Michigan':'MI'}
print(states)
cities = {"CA":"SanFrancisco", "MI":"Detroit", "FL":"Jacksonville"}
print(cities)
cities["NY"] = "New York"
cities["OR"] = "Portland"
print(cities)
print("_" * 10)
print("NY state has: ",cities["NY"])
print("OR state has:", cities["OR"])
print("_" * 10)
print("Michigan's abbreviation is:", states["Michigan"])
print("Florida's abbreviation is:", states["Florida"])
print("-" * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    print('-' * 10)
# safely get a abbreviation by state that might not be there
    state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")
    city = cities.get('TX', 'Does Not Exist')
    print(f"The city for the state 'TX' is: {city}")    