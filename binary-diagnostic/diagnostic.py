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
# Note: I'm gambling that there is not an even number of 1s and 0s in each position
# since the rules don't say anything about tiebreakers! 
def part_one_b(sums):
    gamma = "" # most common bit
    epsilon = "" # least common bit
    for i in range(len(sums)):
        if sums[i] > 500:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)


# for each line, check the value of each bit
# if the bit is one, increment a counter for ones
# else (if the bit is zero), increment a counter for zeroes?
# compare the total number of zeroes in each bit to the number of ones,
# whichever is bigger gets put in an array/list of the appropriate length

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

if __name__ == "__main__":
    # print(load_input("data.txt"))
    # print(len(load_input("data.txt")))
    print(part_one_a(load_input("data.txt")))
    print(part_one_b(part_one_a(load_input("data.txt"))))
