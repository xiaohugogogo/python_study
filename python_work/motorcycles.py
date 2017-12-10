motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('abc')
print(motorcycles)

motorcycles.insert(0, 'abc')
print(motorcycles)

motorcycles.insert(5, 'def')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

pop_element = motorcycles.pop()
print(motorcycles)
print(pop_element)

pop_element = motorcycles.pop(0)
print(motorcycles)
print(pop_element)

del_element = 'abc'
motorcycles.remove(del_element)
print(motorcycles)
print(del_element)

