# motocycles = ['honda','yamaha','suzuki']
# print(motocycles)

# motocycles.append('ducati')
# print(motocycles)

# motocycles[0] = 'ducati'
# print(motocycles)

motocycles = []
# Add an item to the end of a List 
motocycles.append('honda')

motocycles.append('yamaha')
motocycles.append('suzuki')

print(motocycles)

motocycles.insert(0, 'ducati')

print(motocycles)
# Delete an item from a given position within a List
del motocycles[0]

print(motocycles)

del motocycles[1]

print(motocycles)

motocycles = ['honda','yamaha','suzuki']

print(motocycles)
#Removes the last item within a List and store it in a variable
popped_motocycle = motocycles.pop()

print(popped_motocycle)