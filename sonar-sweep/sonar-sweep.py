import itertools
with open('data.txt') as f:
    depths = [int(i) for i in f]
    counter = 0
    prevDepth = depths[0]
    for currentDepth in itertools.islice(depths, 1, None):
        # print("Previous Depth is: " + str(prevDepth))
        # print("Current Depth is: " + str(currentDepth))
        # print("Is the current depth deeper than the previous depth?")
        if currentDepth > prevDepth:
            counter += 1
        #     print("Yes, the current depth is deeper.")
        # else:
        #     print("No, the current depth is not deeper")
        # print("The total number of times the depth has decreased is: " + str(counter))
        prevDepth = currentDepth
    print("The depth has increased " + str(counter) + " times.")
