
def double(arg):
    print("Before: ", arg)
    arg = arg * 2
    print("After: ", arg)


def change(arg):
    print("Before: ", arg)
    arg.append("Test data")
    print("After: ", arg)
