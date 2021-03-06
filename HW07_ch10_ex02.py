
#!/usr/bin/env python3
# <filename>

# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################
# Imports


# Body
def capitalize_nested(list):

    # list loop
    for item in list:
        if type(item) == type([]):
            # for itm in item:
                # if type(item) == type([]):
            return capitalize_nested(item)
                    # test that it reads
        else:
            capitalized = item.capitalize()
            # print(capitalized)
            return capitalized


##############################################################################
def main():

    # capitalize_nested(['a','b','c',['a','b']])
    l = ['apple', ['bear','sloth'], 'cat']
    # for item in l:
    print(capitalize_nested(l))

    #TODO: try calling and printing loop down here first


if __name__ == '__main__':
    main()
