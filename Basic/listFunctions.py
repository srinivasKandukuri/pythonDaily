######### List slicing in Python   ##############

my_list = ['p','r','o','g','r','a','m','i','z']

# elements 3rd to 5th
print(my_list[2:5])


# elements beginning to 4th
print(my_list[:-5])

#

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])


#O/P


# ['o', 'g', 'r']
# ['p', 'r', 'o', 'g']
# ['a', 'm', 'i', 'z']
# ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z']


############ Add/Change List Elements


# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

print(odd)             


Output

[1, 4, 6, 8]
[1, 3, 5, 7]




# Appending and Extending lists in Python
odd = [1, 3, 5]

odd.append(7)

print(odd)

odd.extend([9, 11, 13])

print(odd)
