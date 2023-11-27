#opening file for reading
with open("C:\\Users\\benko\\Downloads\\rosalind_ini2.txt", "r") as file:
    lines = file.readlines()

#make sure the file is seperated by lines
if len(lines) >= 1:
    #split the line and convert to integers
    numbers = [int(num) for num in lines[0].split()]

    if len(numbers) >= 2:
        #take out numbers
        num1 = numbers[0]
        num2 = numbers[1]

        #square them
        square1 = num1 ** 2
        square2 = num2 ** 2

        #add squaress
        result = square1 + square2

        #print result
        print("The sum of the squares is:", result)
