with open('data.txt') as depths:
    data = depths.read()
    print(data)

# questions: since the list is 1000s of values long, what's the most efficient way to do this? Should I sort the list? Or wouldn't that defeat the whole purpose, since it represnts the ocean floor, and you can't order that?
# also, how do I pass the data through this one at a time?
# basic sketch of algo:
    # in goes value
    # if value is bigger than preious value
        # increment counter
    # otherwise, move on to next value / repeat algo
# How many measurements are larger than the previous measurement?
