# Create a program which will accept a string
# and checks whether string is in camelCase
# snake_case and also create two functons
# getCamelCase() and get_snake_case() to convert
# snake_case into camel_case or vice versa

from inflection import camelize, underscore

def check_case(string):
    if '_' in string and any(x.isupper() for x in string):
        print(string, 'is of both snake_case and camelCase! Please provide proper string in 1 format!')
    elif '_' in string:
        print(string, 'is of snake_case!')
    elif any(x.isupper() for x in string):
        print(string, 'is of camelCase!')

def get_camelCase(string):
    str_list = string.split('_')
    result = str_list[0]
    result = result + result.join([str_list[x].capitalize() for x in range(1,len(str_list))])
    return result

def get_snake_case(string):
    return underscore(string)


str1 = 'helloWorld'
str2 = 'hello_world'

check_case(str1)
check_case(str2)

print(get_camelCase(str2))
print(get_snake_case(str1))
