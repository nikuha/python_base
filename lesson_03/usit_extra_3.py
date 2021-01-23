def str_to_upper(s):
    #  вариант через ord
    modified_word = ''
    for k, v in enumerate(s):
        # для латиницы и кириллицы
        if k == 0 and (97 <= ord(v) <= 122 or 1072 <= ord(v) <= 1103):
            modified_word += chr(ord(v) - 32)
        else:
            modified_word += v
    return modified_word


def sentence_to_upper(input_str):
    modified_list = []
    for s in input_str.split(' '):
        modified_list.append(str_to_upper(s))
    return ' '.join(modified_list)


print(sentence_to_upper(input('Введите слова, разделенные пробелом:\n')))