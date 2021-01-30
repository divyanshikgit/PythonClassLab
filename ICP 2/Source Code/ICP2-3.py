infile = open("word.txt", 'r')          # Access the file

count = dict()          # creating a dictionary variable

for lines in infile:
    lines = lines.strip()
    word = lines.split(" ")   #Splitting Each line
    for letters in word:
        if letters in count:
            count[letters] = count[letters] + 1            # If word id present in dictionary, update the count
        else:
            count[letters] = 1


print("Word count = ")
for letters in count:
    print(letters, " ", count[letters])         # Print the count present