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
