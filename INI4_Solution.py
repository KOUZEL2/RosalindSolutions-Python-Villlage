#opening file for reading
file = open("C:\\Users\\benko\\Downloads\\rosalind_ini4 (5).txt", "r")
#determine a and b
lines=file.readlines()
if len(lines) >= 1:
    # Split the line using spaces and convert to integers
    numbers = [int(num) for num in lines[0].split()]

    if len(numbers) >= 2:
        # Extract the numbers
        a = numbers[0]
        b = numbers[1]
        print(a,b)

        #Perform the required math which is sum of all odd between a and b
        c = a - b
        #creating numbers between a and b
        n = a
        print(n)
        list = []
        if a % 2 == 1:
            list.append(n)
        while n < b:
            iterater = 1 + n
            n = iterater
            #checking if the value is odd then adding it to the list
            if n % 2 == 1:
                list.append(n)
            
        #suming list
        total = sum(list)
        print(list)
       
        print("The sum of odd numbers between a and b is:", total)
    else:
        print("The file does not contain at least two numbers.")
else:
    print("The file is empty.")
