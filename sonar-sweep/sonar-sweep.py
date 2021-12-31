def load_input(data):
    with open(data) as f:
        depths = [int(i) for i in f]
        return depths

#~~~~~~~~~~~~ naive solutions ~~~~~~~~~~~~~~~~~~~~#

def sonar_sweep_part_one(depths):
    counter = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            counter += 1
    print(f"The depth has increased {counter} times.")

def sonar_sweep_part_two(depths):
    counter = 0
    for i in range(1, len(depths)-2):
        if depths[i] + depths[i+1] + depths[i+2] > depths[i-1] + depths[i] + depths[i+1]:
            counter += 1
    print(f"The sum of three consecutive depths has increased {counter} times.")

#~~~~~~~~~~ solutions using zip ~~~~~~~~~~~~~~~~~#

def sonar_sweep_part_one_zip(depths):
    counter = 0
    for prevDepth, currentDepth in zip(depths, depths[1:]):
        if currentDepth > prevDepth:
            counter += 1
    print(f"The depth has increased {counter} times.")

# def sonar_sweep_part_two_zip(depths):


#~~~~~~~~~~ solutions using list comprehension ~~~~~~~~~~~~~~~~~#

def sonar_sweep_part_one_comprehension(depths):
    depthIncreases = [1 for (left, right) in zip(depths, depths[1:]) if right > left]
    print(f"The depth has increased {len(depthIncreases)} times.")

# def sonar_sweep_part_two_comprehension(depths):

#~~~~~~~~~~~~~~~~solutions using sum/zip~~~~~~~~~~~~~~~~~~~~~~~~#

def sonar_sweep_part_one_sum(depths):
    return sum(1 for (left, right) in zip(depths, depths[1:]) if right > left)


if __name__ == "__main__":
    sonar_sweep_part_one(load_input('data.txt'))
    sonar_sweep_part_two(load_input('data.txt'))
    sonar_sweep_part_one_zip(load_input('data.txt'))
    sonar_sweep_part_one_comprehension(load_input('data.txt'))
    print(sonar_sweep_part_one_sum(load_input('data.txt')))
