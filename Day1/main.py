# Chronal Calibration

# Import input data
with open("input.txt", "r") as input:
    data = input.read().split('\n')

# Part One - calculate frequency changes
def PartOne():
    frequency = 0

    ## For each item in data, split the operator from the number
    for row in data:
        if row[0] == '+':
            frequency += int(row[1:])
        if row[0] == '-':
            frequency -= int(row[1:])

    print(frequency)

    # 484 is the answer.

## Part Two: Find the first frequency that happens twice.
def PartTwo():
    current_frequency = 0
    frequencies = [0]
    solved = False

    def RunList(frequency, all_frequencies):
        freq = int(frequency)
        all_freq = all_frequencies
        for row in data:
            if row[0] == '+':
                freq += int(row[1:])
                # Check to see if the frequency is already in our list
                if freq not in all_freq:
                    # Add the frequency to our frequency list
                    all_freq.append(freq)
                    # print(f'adding frequency {freq}')
                else:
                    return (freq, all_freq, True)
                
            if row[0] == '-':
                freq -= int(row[1:])
                            # Check to see if the frequency is already in our list
                if freq not in all_freq:
                    # Add the frequency to our frequency list
                    all_freq.append(freq)
                    # print(f'adding frequency {freq}')
                else:
                    return (freq, all_freq, True)
        return (freq, all_freq, False)



    while 1==1:
        frequency, all_frequencies, solved = RunList(current_frequency, frequencies)
        if solved == True:
            print(frequency)
            break
        current_frequency = frequency
        frequencies = all_frequencies
        print("Next loop")
        # print(current_frequency, len(frequencies), len(set(frequencies)))
        # all_frequencies.sort()
        # print(all_frequencies)
        # break
    print(frequency)
    # This runs very slowly, but yields 367 as the answer (which is correct).
            
PartTwo()






