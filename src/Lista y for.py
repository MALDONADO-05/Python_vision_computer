cars = ["bmw", "bucho"]
prices = ["1", "5"]
print(cars) # ['bmw', 'bucho']
print(cars[0])
print(f"Mi primer carro fue un {cars[0]}")
print(f"Mi primer carro fue un {cars[1]}")
# car es un elemento de la lista, es una variable string
for car in cars:
    print(f"Mi primer carro fue {car}")

for ind,value in enumerate (cars):
    print(ind,value)



for car, prices in zip(cars,prices):
    print(car,prices)

