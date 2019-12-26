# A program which accepts a string and
# returns the string with all the surrounding
# duplicates removed it
# E.g., "NEEXXxTTGGEENNNCCOODEERR" -> "NEXxTGENCODER"


def remove_duplicates(string):
    str_list = list()
    x = string[0]
    str_list.append(x)
    for i in range(1, len(string)):
        if x != string[i]:
            str_list.append(string[i])
        x = string[i]
    return "".join(str_list)


string = "NEEXXxTTGGEENNNCCOODEERR"
print(remove_duplicates(string))
