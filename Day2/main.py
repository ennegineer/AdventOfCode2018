# Day 2 : Inventory Management System

# Import the data
with open("input.txt", "r") as input:
    data = input.read().split('\n')
    
# Parse the data then count how many boxes have a letter appearing exactly twice, and how many have a letter appearing exactly 3 times. multiply these together for the answer (checksum)

def PartOne():
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

# 5166 is the answer

# Part Two!
## Find the two boxes with only one mismatched character (and in the same order).
## What letters are common between the two correct box IDs?

def PartTwo():
    answer = ''
    # Set up boxes to compare
    box_one = ''
    box_two = ''
    # Loop through the data, and for each one, loop through the data again to look for a match of all but one character. 
    for row in data:
        # Set up the next box.
        box_one = row
        # Loop through the boxes again to assign box two.
        # (need to clean this up to skip the rows we've already compared to save resources)
        for row in data:
            # if row == box_one:
            #     pass
            # else:
            # Set up the second box and reset the mismatches to 0.
            box_two = row
            mismatches = 0

            # Compare each item in both boxes, in order.
            for x in range(0, len(box_one)):
                if box_one[x] != box_two[x]:
                    mismatches += 1
            if mismatches == 1:
                print(f' Box 1: {box_one} \n Box 2: {box_two} \n mismatches: {mismatches}')
                break
    # this is not working. need to fix.
    for x in range(0, len(box_one)):
        if box_one[x] != box_two[x]:
            answer = box_one[:x] + box_one[x+1:]
    print(answer)
PartTwo()


