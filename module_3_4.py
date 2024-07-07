# Произвольное число параметров

# 1.Функция подбора однокоренных слов:
def single_root_words(root_word, *other_words):
    if type(root_word) is not str:
        print(root_word, ' не является строковой переменной')
    root_word = root_word.lower()
    same_words = []
    for word in other_words:
        if type(word) is str and (root_word in word.lower() or word.lower() in root_word):
            same_words += [word]

    return same_words

#root_word_ = 'смеЛ'
#other_words_ = 'Смелость', 'посметь', 'осмелеть', True
#rint(single_root_words(root_word_, *other_words_))

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


