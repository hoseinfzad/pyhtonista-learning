cars = ['bmw','audi','toyota','subaru']
# print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# array.sort() sorts the list permamently and sorted() sorts tempararly

print("Here is the original list: ")
print(cars)

print("\nHere is the Sorted list: ")
print(sorted(cars))

print("\nHere is the original list again: ")
print(cars)

print("\nHere is the Sorted new cars list: ")
new_cars = sorted(cars)

print(new_cars)

new_cars.reverse()
print(new_cars)

# To find the length of an array use the len() method: len(array)
print(len(cars))

