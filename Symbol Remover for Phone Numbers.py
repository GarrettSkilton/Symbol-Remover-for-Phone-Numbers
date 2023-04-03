number_with_symbols = '5+(555)-555-5555'
for number_with_symbols in number_with_symbols:
    if number_with_symbols == '-':
        continue
    elif number_with_symbols == '(':
        continue
    elif number_with_symbols == ')':
        continue
    elif number_with_symbols == '+':
        continue
    else :
        print(number_with_symbols, end='')