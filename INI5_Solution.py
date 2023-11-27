#opening file for reading
file = open("C:\\Users\\benko\\Downloads\\rosalind_ini5 (2).txt", "r")
#extracting all the lines
lines=file.readlines()
#determine the length
max=len(lines)
#seperating even
list_evens = []
for i in range(1, max, 2):
    list_evens.append(lines[i])
    
for line in list_evens:
    print(line)