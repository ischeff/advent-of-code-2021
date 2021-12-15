import itertools
with open('data.txt') as f:
    depths = [int(i) for i in f]
    # data = depths.read()
    # print(data)
    # prevDepth = depths[0]
    counter = 0
    # currentDepth = 0
    for currentDepth in itertools.islice(depths, 1, None):
        print("Previous Depth is: " + str(prevDepth))
        print("Current Depth is: " + str(currentDepth))
        print("Is the current depth deeper than the previous depth?")
        if currentDepth > prevDepth:
            counter = counter + 1
            print("Yes, the current depth is deeper.")
        else:
            print("No, the current depth is not deeper")
        currentDepth = prevDepth
    print("The depth has increased " + str(counter - 1) + " times.")


# questions: since the list is 1000s of values long, what's the most efficient way to do this? Should I sort the list? Or wouldn't that defeat the whole purpose, since it represnts the ocean floor, and you can't order that?
# also, how do I pass the data through this one at a time?
# basic sketch of algo:
    # in goes value
    # if value is bigger than preious value
        # increment counter
    # otherwise, move on to next value / repeat algo
# How many measurements are larger than the previous measurement?
