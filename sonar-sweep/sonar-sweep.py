import itertools

# below is the first draft solution
# def sonar_sweep_part_one():
#     with open('data.txt') as f:
#         depths = [int(i) for i in f]
#         counter = 0
#         prevDepth = depths[0]
#         for currentDepth in itertools.islice(depths, 1, None):
#             # print("Previous Depth is: " + str(prevDepth))
#             # print("Current Depth is: " + str(currentDepth))
#             # print("Is the current depth deeper than the previous depth?")
#             if currentDepth > prevDepth:
#                 counter += 1
#             #     print("Yes, the current depth is deeper.")
#             # else:
#             #     print("No, the current depth is not deeper")
#             # print("The total number of times the depth has decreased is: " + str(counter))
#             prevDepth = currentDepth
#         print(f"The depth has increased {counter} times.")

# below is some refactoring based on feedback from my friend Will
def load_input(data):
    with open(data) as f:
        depths = [int(i) for i in f]
        return depths

def sonar_sweep_part1_revised(depths):
    counter = 0
    prevDepth = depths[0]
    for currentDepth in itertools.islice(depths, 1, None):
        if currentDepth > prevDepth:
            counter += 1
        prevDepth = currentDepth
    print(f"The depth has increased {counter} times.")

def sonar_sweep_part1_zip(depths):
    # print(zip(depths, itertools.islice(depths, 1, None)))
    counter = 0
    for prevDepth, currentDepth in zip(depths, itertools.islice(depths, 1, None)): # still not totally sure how zip is working
        if currentDepth > prevDepth:
            counter += 1
        prevDepth = currentDepth
    print(f"The depth has increased {counter} times.")

def sonar_sweep_part1_comprehension(depths):
    depthIncreases = [1 for (left, right) in zip(depths, depths[1:]) if right > left]
    print(f"The depth has increased {len(depthIncreases)} times.")
    return len(depthIncreases)

def sonar_sweep_part1_liner(depths):
    return sum(1 for (left, right) in zip(depths, depths[1:]) if right > left)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def sonar_sweep_part_two(depths):
    counter = 0
    # for i in itertools.islice(depths, 1, len(depths)-3):
    for i in zi[(depths)]
        if depths[i] + depths[i + 1] + depths[i + 2] > depths[i - 1] + depths[i] + depths[i + 1]:
            counter += 1
    print(f"The sum of three consecutive depths has increased {counter} times.")

        # check if sum is greater than previous group of three
        # return something
        # move to next group of three



if __name__ == "__main__":
    # sonar_sweep_part_one()
    sonar_sweep_part1_revised(load_input('data.txt'))
    sonar_sweep_part1_zip(load_input('data.txt'))
    sonar_sweep_part1_comprehension(load_input('data.txt'))
    print(sonar_sweep_part1_liner(load_input('data.txt')))
    sonar_sweep_part_two(load_input('data.txt'))
