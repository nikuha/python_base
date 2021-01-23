def str_to_upper(s):
    return s.capitalize()

    # вариант 2 через первый символ
    # return s[0].upper() + (s[1:] if len(s) > 1 else '')

    #  вариант 3 напрямую через цикл
    # modified_word = ''
    # for k, v in enumerate(s):
    #     modified_word += v.upper() if (k == 0) else v
    # return modified_word


def sentence_to_upper(input_str):
    modified_list = []
    for s in input_str.split(' '):
        modified_list.append(str_to_upper(s))
    return ' '.join(modified_list)


print(sentence_to_upper(input('Введите слова, разделенные пробелом:\n')))