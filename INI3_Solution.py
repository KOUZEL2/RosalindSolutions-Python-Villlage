#opening file for reading
file = open("C:\\Users\\benko\\Downloads\\rosalind_ini3 (2).txt", "r")
#seperate lines
lines=file.readlines()
LineOne = lines[0]
LineTwo = lines[1]
#have to properly extract the numbers from line two
NumberExtract = LineTwo.split()
print(LineOne)
print(LineTwo)
print(NumberExtract)
#now to convert the second line into indicies
a = int(NumberExtract[0])
b = int(NumberExtract[1])
c = int(NumberExtract[2])
d = int(NumberExtract[3])

print(a,b,c,d)
#slice the first line by the indices listed
LettersOne = LineOne[a:(b+1)]
LettersTwo = LineOne[c:(d+1)]
print(LettersOne, LettersTwo)
