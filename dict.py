# cars = {'corola': "red", 'fit': "green", '320': "black"}

cars = {}

cars['corolla'] = "red"
cars['fit'] = "green"
cars['320'] = "black"

#cars.keys()
#cars.values()
#cars['corola']

for car in cars:
    print(car + " = " + cars[car])

for key, value in cars.items():
    print(key + " = " + value)


people = dict(Andre='Father', Tatiane='Mother', Pedro='baby')

if 'Andre' in people:
    print(people['Andre'])

