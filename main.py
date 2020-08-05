import random
import argparse
from sys import argv
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "{}[]()!@#$%^&*()_+=-\|:;'""<>,./?"

all = lower + upper + numbers + symbols
parse = argparse.ArgumentParser(description="Random Password Generator")
parse.add_argument('-l', "--length", help=" Length of Password", type=int)
arg = parse.parse_args()
length = arg.length

banner = """    =============================
    | Random Password Generator |
    ============================="""

hlp = """
    Usage : python3 main.py -l <lenght>
    Example : python3 main.py -l 16
    """

def passwd(length):
    password = "".join(random.sample(all, length))
    print(f"{banner}\n\n  => Your Password : {password}")


if __name__ == "__main__":
    if len(argv) != 3:
        print(banner + hlp)
    else:
        passwd(length)
