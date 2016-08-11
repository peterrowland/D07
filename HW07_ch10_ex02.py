
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
    if type(list) == type([]):
        for item in list:
            if type(item) == type([]):
                capitalize_nested(item)
                # test that it reads
            else:
                capitalized = item.capitalize()
                print(capitalized)
                # return capitalized


# if list: enter innerloop on sublist
    # run capitalize on sub list
# if string: run capitalize on list[n]

# return capitalized list

##############################################################################
def main():

    # capitalize_nested(['a','b','c',['a','b']])
    l = capitalize_nested(['apple', ['bear','sloth'], 'cat'])
    print(l)
    #TODO: try calling and printing loop down here first


if __name__ == '__main__':
    main()
