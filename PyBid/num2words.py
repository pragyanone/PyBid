def num2words(num):
    """
    Returns the word for a number. The usual percentages are from 25 to 75.
    """
    ones = {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
    }

    tens = {
        "2": "Twenty",
        "3": "Thirty",
        "4": "Forty",
        "5": "Fifty",
        "6": "Sixty",
        "7": "Seventy",
        "8": "Eighty",
        "9": "Ninety",
    }

    if len(num) == 1:
        return ones[num]
    elif len(num) == 2:
        if num[1] == "0":
            return tens[num[0]]
        else:
            return tens[num[0]] + "-" + ones[num[1]]


if __name__ == "__main__":
    help(num2words)
    for i in range(1, 10):
        print(num2words(str(i)), end="\t")
    for i in range(20, 100, 10):
        print("\n")
        for j in range(10):
            print(num2words(str(i + j)), end="\t")


def ordinal(num):
    ordinals = {
        "1": "First",
        "2": "Second",
        "3": "Third",
    }
    return ordinals[num]
