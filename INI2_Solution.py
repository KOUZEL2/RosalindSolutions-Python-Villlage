# Open the text file for reading
with open("C:\\Users\\benko\\Downloads\\rosalind_ini2.txt", "r") as file:
    lines = file.readlines()

# Ensure there is at least one line in the file
if len(lines) >= 1:
    # Split the line using spaces and convert to integers
    numbers = [int(num) for num in lines[0].split()]

    if len(numbers) >= 2:
        # Extract the numbers
        num1 = numbers[0]
        num2 = numbers[1]

        # Square the numbers
        square1 = num1 ** 2
        square2 = num2 ** 2

        # Add the squares
        result = square1 + square2

        # Print the result
        print("The sum of the squares is:", result)
    else:
        print("The file does not contain at least two numbers.")
else:
    print("The file is empty.")