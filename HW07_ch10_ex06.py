
#!/usr/bin/env python3
# <filename>

# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

##############################################################################
# Imports
# copy

# Body

def is_sorted(in_list):
    # Try/except list sorting
    try:
        sorted(in_list)
    except:
        print('not sortable')

    else:
        if sorted(in_list) != in_list:
            return False

        #TODO: check reverse sorting
        # elif sorted(in_list, reverse=True) != in_list:
        #     return False

        else:
            return True


# if list == list.sort()
    # return true

# also check if reverse sort is true

# else false


##############################################################################
def main():
    pass

if __name__ == '__main__':
    main()
