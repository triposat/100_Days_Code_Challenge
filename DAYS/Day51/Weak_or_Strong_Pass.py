import re


def password(Given_Pass):

    if Given_Pass == "\n" or Given_Pass == " ":
        return "Password cannot be a newline or space"

    if 9 <= len(Given_Pass) <= 20:

        if re.search(r'(.)\1\1', Given_Pass):
            return "Sorry, Weak Password - Same character repeats three or more times in a row"

        if re.search(r'(..)(.*?)\1', Given_Pass):
            return "Sorry, Weak Password - Same string pattern repetition"

        else:
            return "Awesome, Strong Password"

    else:
        return "Password length must be 9-20 characters"


if __name__ == "__main__":
    print(password("Qggf!@ghf3"))
    print(password("Gggksforgeeks"))
    print(password("aaabnil1gu"))
    print(password("Aasd!feasn"))
    print(password("772*hd897"))
    print(password(" "))
