def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def on_ask_change(password):
    function_list = [has_digit, has_letters, is_very_long, has_upper_letters, has_lower_letters, has_symbols]
    score = 0
    for function in function_list:
        if function(password):
            score += 2
    return score


def main():
    password = input('Введите пароль: ')
    print('Рейтинг пароля:', on_ask_change(password))


if __name__ == '__main__':
    main()
