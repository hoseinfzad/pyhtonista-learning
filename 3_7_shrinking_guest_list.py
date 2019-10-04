guess_list = []

guess_list.append('Andree')
guess_list.append('Paulette')
guess_list.append('Azlinah')
guess_list.append('Nhat')

popped_guess =  guess_list.pop(3)
guess_list.append('Chan')

guess_list.insert(0, 'Azure')
guess_list.insert(3, 'Shena')
guess_list.append('Rosa Lee')

print("Hello everyone I've found a bigger table\n")

print("Hello " + guess_list[0] +  " you are invited to the dinner party!\n")
print("Hello " + guess_list[1] +  " you are invited to the dinner party!\n")
print("Hello " + guess_list[2] +  " you are invited to the dinner party!\n")
print("Hello " + guess_list[3] +  " you are invited to the dinner party!\n")
print("Hello " + guess_list[4] +  " you are invited to the dinner party!\n")
print("Hello " + guess_list[5] +  " you are invited to the dinner party!\n")
print("Hello " + guess_list[6] +  " you are invited to the dinner party!\n")

print(popped_guess + " could'nt make it to the dinner party")

print(guess_list)

popped_guess_1 = guess_list.pop(0)
print("Sorry for the inconvience " + popped_guess_1 + " the bigger table hasnt arrived\n")
# print(guess_list)

popped_guess_2 = guess_list.pop(2)
print("Sorry for the inconvience " + popped_guess_2 + " the bigger table hasnt arrived\n")
# print(guess_list)

popped_guess_3 = guess_list.pop(2)
print("Sorry for the inconvience " + popped_guess_3 + " the bigger table hasnt arrived\n")
# print(guess_list)

popped_guess_4 = guess_list.pop(2)
print("Sorry for the inconvience " + popped_guess_2 + " the bigger table hasnt arrived\n")
# print(guess_list)

popped_guess_5 = guess_list.pop(2)
print("Sorry for the inconvience " + popped_guess_5 + " the bigger table hasnt arrived\n")
# print(guess_list)