def load_input(data):
    with open(data) as f:
        course = [str(i) for i in f]
        return course

#~~~~~~~~~~~~~~~~~~~~~ naive solutions ~~~~~~~~~~~~~~~~~~~~~~~~~~#

def part_one(course):
    x = 0
    y = 0
    for line in course:
        direction, magnitude = line.split()
        magnitude = int(magnitude)
        if direction.startswith("f"):
            x += magnitude
        elif direction.startswith("d"):
            y += magnitude
        else:
            y -= magnitude
    return x * y


# get the input
# how should you process it?
# input is [forward/up/down NUM]
# you want to check line by line to see what letter it starts with - use line.startswith("s") or whatever else
# then you need to check for the number - how do you do that? should you pull it out? make a separate list?

# create empty placeholders for coordinates--vertical/horizontal position

# for every line:
    # if the line starts with "f", add number that follows to x coordinate (horizontal)
    # if the line starts with "d", add number that follows to y coordinate (vertical)
    # else (if the line starts with "u"), subtract number that follows from y coordinate (vertical)

# assign variable to product of final coordinates

if __name__ == "__main__":
    # print(load_input("data.txt"))
    print(part_one(load_input("data.txt")))
