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
        if sums[i] > len(report)/2: # 1 is most common
            gamma += "1"
            epsilon += "0"
        else: # 0 is most common
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

# sketch of part 2
# maybe make oxygen an empty list and CO2 an empty list
# try using a list comprehension to filter report -

def test(report, x):
    print(report[x])
    line = report[x]
    for bit in line:
        print(bit)

    #     line = report[i]
    #     for j in line:
    #         print line[j]
    # print(report[x][1])
# def part_two(sums, report):
#     oxygen = [x for x in report] # most common bit
#     carbon_dioxide = [x for x in report] # least common bit
#     for i in range(len(sums)):
#         # line_oxygen = oxygen[i]
#         # line_carbon_dioxide = carbon_dioxide[i]
#         if sums[i] >= len(report)/2: # 1 is most common
#             oxygen = [x for x in oxygen if oxygen[i] == "1"]
#             carbon_dioxide = [x for x in carbon_dioxide if carbon_dioxide[i] == "0"]
#         else: # 0 is most common
#             oxygen = [x for x in oxygen if oxygen[i] == "0"]
#             carbon_dioxide = [x for x in carbon_dioxide if carbon_dioxide[i] == "1"]
#     return oxygen, carbon_dioxide

# def part_two(sums, report):
#     # make two copies of report (one for oxygen and one for C02)
#     oxygen = [x for x in report]
#     co2 = [x for x in report]
#     for i in range(len(sums)):
#         if sums[i] >= len(report)/2:
#             oxygen = [x for x in oxygen if oxygen[i] != "1"]
#             c02 = [x for x in co2 if co2[i] != "0"]
#         else:
#              oxygen = [x for x in oxygen if oxygen[i] != "0"]
#              c02 = [x for x in co2 if co2[i] != "1"]
#         return oxygen, c02
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
    # print(part_two(part_one_a(load_input("data.txt")), load_input("data.txt")))
    test(load_input("data.txt"), 2)
