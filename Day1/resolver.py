
allNumbers = ['0','1','2','3','4','5','6','7','8','9']
# Open the file in read mode
with open('./Day1/Input.txt', 'r') as file:
    allTwoDigitNumbers = []
    # Read each line in the file
    for line in file:
        # Process the line (replace this with your own logic)
        allNumbersInLine = []
        for character in line:
            if character in allNumbers:
                allNumbersInLine.append(character)
        
        firstNumber = int(allNumbersInLine[0]) *10
        lastNumber = int(allNumbersInLine[len(allNumbersInLine)-1])

        completeTwoDigitNumber = firstNumber + lastNumber
        allTwoDigitNumbers.append(completeTwoDigitNumber)
    
    # Sum all two digit numbers
    sum = 0
    for number in allTwoDigitNumbers:
        sum += number
    
    # Print the result
    print(sum)

