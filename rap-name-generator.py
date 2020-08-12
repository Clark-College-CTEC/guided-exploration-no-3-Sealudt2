# Guided Exploration No. 3
# Calvin Hart

# Imports random library
import random

# Initiates an empty list for possible rap names
possible_names = []

# Opens new file that will store generated results
outputFile = open('rap-names-output.txt', 'w')

# Opens the text file as "datafile" to be altered
with open('rap-names.txt', 'r') as dataFile:
    # for loop to cycle through the code in datafile one at a time
    for name in dataFile:
        # append the possible_names list and apply to the rstrip method to every name in the loop.
        possible_names.append(name.rstrip())

# Prompt user to enter how many rap names they would like to create
count = int(input('How many rap names would you like to create? '))
# Enter how many parts they want the name to contain
parts = int(input('How many parts should the name contain? '))

# counted loop that cycles based on the number of names the user wants to create
for i in range(count):
    # initiate an empty list that holds the rap name parts accumulated by the loop below
    name_parts = []
    # counted loop that returns the number of rap name parts requested
    for j in range(parts):
        # append the parts of the name to the list of possible rap names which is randomized based on the length
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

        # taking name parts generated from loop and gluing them to the file in which generates rap names
        outputFile.write(f"{' '.join(name_parts)}\n")
        # print the results
        print(f"{' '.join(name_parts)}")
# close open file to complete infile writing
outputFile.close()
