import sys


try:
    if len(sys.argv) != 2:
        raise AssertionError(
            "Invalid number of arguments. Please enter only one argument!"
        )
    av1: str = sys.argv[1]
    if (
        not (len(av1) != 1 and av1[0] == "-" and str(av1[1]).isnumeric())
        and not av1.isnumeric()
    ):
        raise ValueError("Invalid argument. Please enter a number!")
except Exception as e:
    print(f"AssertionError: {e}")

else:
    av1 = int(av1)
    if av1 % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
