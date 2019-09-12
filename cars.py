import json

filename = 'cars_file.json'
with open(filename,'r') as f1:
    cars = json.loads(f1.read())
f1.close()
print('Input a car name and model separated by space (for example: ford sierra,opel astra) that you are looking for:')
input_val = str(input())
if input_val in cars.keys():
    print('We have this car and it cost\'s %.2f USD' % cars.get(input_val))
else:
    print('We don\'t have this car.Please type car\'s price and currency (USD,EUR,GPB) for that price separated by space:')
    new_car = str(input())
    temp_list = new_car.split()
    price = int(temp_list[0])
    currency = temp_list[1]
    if currency == 'EUR' or 'eur':
        price *= 0.91
    elif currency == 'GPB' or 'gpb':
        price *= 0.81
    print('That car cost\'s %.2f USD' % price)
    cars.update({input_val:price})
with open(filename,'w') as f2:
    f2.write(json.dumps(cars,sort_keys=True,indent=3))
f2.close()
