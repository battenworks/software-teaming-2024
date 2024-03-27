roman_numerals = {
    10: 'X',
    5: 'V',
    1: 'I'
}


def convert_to_roman(number):
    result = ''
    
    for key, value in roman_numerals.items():
        if number == key:
            result += value
            return result
        elif number == (key - 1):
            result += ('I' + value)
            number -= key
            return result
        
        while number >= key:
            result += value
            number -= key

    return result

    # for key, value in roman_numerals.items():
    #     if number == key:
    #         return value
    #     elif number / key == 2:
    #         return value + value
    #     elif number == (key - 1):
    #         return 'I' + value
    #     elif number > key:
    #         result = value
    #         while number > key:
    #             number -= 1
    #             result += 'I'
            
    #         return result
