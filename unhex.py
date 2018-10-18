
def make_hexdict():
    hexdict = ['a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15]

    for i in range (0, 9):
        hexdict[str(i)] = i

    print(hexdict)


def unhex(string):
    hexdict = make_hexdict()
    ans = 0

    # Sometimes hex numbers are prefixed with "0x", ex. "0xfff" to show that they are hex.
    # We want this function to work regardless of whether this prefix is there or not.
    # So, if the prefix is there, we just remove it.
    if string[:2] == "0x":
        string = string[1:]

    for i in range (0, len(string)):
        position_power = 16**(len(string)-1-i)
        curr_digit = hexdict(string[i])
        ans += curr_digit * position_power

    print(ans)


def main():
    user_input = ""
    while user_input != "quit" and user_input != "q":
        user_input = input("> ")
        print(unhex(str(user_input)))
