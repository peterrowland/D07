#!/usr/bin/env python3
# I want to be able to call cumulative_sum from main w/ various lists and
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################
# Imports


# Body
def cumulative_sum(in_list):
    sum_list = []
    idx = 0
    for i in range(len(in_list)):
        if i == 0:
            sum_list.append(in_list[i])
        else:
            cumulative = sum_list[i-1] + in_list[i]
            sum_list.append(cumulative)

    return sum_list

# Make a new list
# add previous item !case if first item
# put sum in cumulative list
# return cumulative list

##############################################################################
def main():
    pass
if __name__ == '__main__':
    main()
