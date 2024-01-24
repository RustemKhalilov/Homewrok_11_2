def Simvol_UP(word):
    """Функция возвращает все буквы слова заглавными"""
    return word.upper()


def Simvol_UP_first(words):
    """Функция возвращает первые буквы слов заглавными"""
    str1 = words.split(" ")
    str_2 = ""
    for item in str1:
        str_2 = str_2 + " " + item[0].upper() + item[1:]
    return str_2



