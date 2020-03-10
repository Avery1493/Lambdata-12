
# my_lambdata/my_mod.py


def enlarge(n):
    """
    Parm n is a number
    Function will enlarge the number
    """
    return n * 100


# this code breaks our ability to import enlarge from other files
# print("HELLO")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))


if __name__ == "__main__":
    # only run this code IF this script is invoked from the command line
    # not if it is imported from another
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))

