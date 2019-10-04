guess_list = []

guess_list.append('Andree')
guess_list.append('Paulette')
guess_list.append('Azlinah')
guess_list.append('Nhat')

popped_guess =  guess_list.pop(3)
guess_list.append('chan')

print("Hello dear " + guess_list[0] +  " you are invited to the dinner party!\n")
print("Hello dear " + guess_list[1] +  " you are invited to the dinner party!\n")
print("Hello dear " + guess_list[2] +  " you are invited to the dinner party!\n")
print("Hello dear " + guess_list[3] +  " you are invited to the dinner party!\n")

print(popped_guess + " could'nt make it to the dinner party")
