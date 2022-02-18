#6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

#7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().


def int_func(word=str):
    return word[0].upper()+word[1:]

def int_sentence(sentence):
    list_sentence=sentence.split()
    new_list_sentence=[]
    new_sentence=''
    for word in list_sentence:
        new_list_sentence.append(int_func(word))
    for word in new_list_sentence:
        new_sentence+=word+' '
    return new_sentence


sentence=input('Введите строку из слов:')
print(int_sentence(sentence))
