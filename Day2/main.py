# Day 2 : Inventory Management System

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')
    
# Parse the data then count how many boxes have a letter appearing exactly twice, and how many have a letter appearing exactly 3 times. multiply these together for the answer (checksum)

def DayOne():
    # Track the boxes that have letters appearing exactly twice or exactly three times.
    twos = 0
    threes = 0
    for row in data:
        two = False
        three = False
        # Check how many times a letter exists in the row. Count those that exist 2 or 3 times.
        test = ''.join(sorted(row))
        for letter in test:
            if test.count(letter) == 2:
                two = True
                test = test.replace(letter, '')
            if test.count(letter) == 3:
                three = True
                test = test.replace(letter, '')
        if two == True:
            twos += 1
        if three == True:
            threes += 1
    # Show the answer!
    checksum = twos * threes
    print(f'{twos} times {threes} = {checksum}')


DayOne()
# 5166 is the answer
