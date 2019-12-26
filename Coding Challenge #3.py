# Take an input as a string and arrange
# it's every characters in alphabetical
# order from A -> Z
# E.g., NextGenCoder -> CdeeeGNnortx

def sorting_characters(string):
    string_list = list(string)
    result_list = sorted(string_list, key=str.casefold)
    result_string = "".join(result_list)
    return result_string


string = "NextGenCoder"
print(sorting_characters(string))