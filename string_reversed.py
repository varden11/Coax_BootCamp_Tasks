def string_reverse(orig_string):
    x = len(orig_string)
    rev_string = ''
    while (x > 0):
        rev_string += orig_string[x - 1]
        x -= 1
    return rev_string
print('This program reverse text that was inputed')
print('Please input some text and press Enter:')
text_input = str(input())
print(string_reverse(text_input))