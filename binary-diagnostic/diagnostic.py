def load_input(data):
    with open(data) as f:
        report = f.readlines()
        return report

#~~~~~~~~~~~~ naive solutions ~~~~~~~~~~~~~~~~~~~~#

def part_one_a(report):
    sums = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(report)):
        line = report[i]
        for j in range(len(line)):
            if line[j] == "1":
                sums[j] += 1
    return sums
# since the len of the report is 1000 lines, if the sum is less than 500,
# the majority of the bits in that column are 0s and vice versa
# Note: I'm gambling that there is not an equal number of 1s and 0s in each position
# since the rules don't say anything about tiebreakers!
def part_one_b(sums, report):
    gamma = "" # most common bit
    epsilon = "" # least common bit
    for i in range(len(sums)):
        if sums[i] > len(report)/2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

# sketch of part 2
# maybe make oxygen an empty list and CO2 an empty list
# try using a list comprehension to filter report -

def part_two(sums, report):
    # make two copies of report (one for oxygen and one for C02)
    #if the sum for a given position is > 500
        # then remove ANY item in oxygen list that does NOT have a 1 at that position
        # then remove ANY item in CO2 that does NOT have a 0 at that position
    #if the sum for a given position is <500
        # then remove ANY item in list that does NOT have a 0 at that position
        # then remove ANY item in CO2 that does NOT have a 1 at that position
    # if the sum for a given position equals 500
        # then remove ANY item in list that does NOT have a 1 at that position
        # then remove ANY item in CO2 that does NOT have a 0 at that position
    # return int(oxygen, 2) * int(C02, 2)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == "__main__":
    # print(load_input("data.txt"))
    # print(len(load_input("data.txt")))
    print(part_one_a(load_input("data.txt")))
    print(part_one_b(part_one_a(load_input("data.txt")), load_input("data.txt")))
