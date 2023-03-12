#######################################################################################################
#Напишите программу, которая получает от пользователя имя файла, открывает этот файл
# в текущем каталоге, читает его и выводит два слова: наиболее часто встречающееся из тех,
# что имеют размер более трех символов, и наиболее длинное слово .
####################################################################################
file = input('Напишите название файла с расширением: ')
with open(file, encoding='utf8') as f:
    file = f.read()
def clean_text(file):
    for i in '!"\'#$%&()*+-,/.:;<=>?@[\\]^_{|}~':
        clean_list = file.replace(i, '')#убираются знаки и заменяются на пустоту
    return file.split()#все слова в тексте файла выводятся в список
clean_list = clean_text(file)
#Убираем все слова менее 3 букв
def long_listfun(clean_list):
    long_list = []
    for i in clean_list:
        if len(i) > 3 :
            long_list.append(i)
    return long_list
long_list = long_listfun(clean_list)
# определяем самое длинное слово в списке
long_word = max(long_list, key=len)
print(f'Самое длинное слово: "{long_word}"')
# Оставляем в списке только английские слова
def english_list_fun():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    english_list = []
    for item in long_list:
        for char in item:
            if char in alphabet:
                charEn = True
            else:
                False
        if charEn:
            english_list.append(item)
    return english_list
english_list = english_list_fun()
#Переводим список в словарь, в значение запишем подсчёт слова
def dictionary_fun():
    diсtionary = {}
    for i in english_list:
        if i in diсtionary:
            diсtionary[i] += 1
        else:
            diсtionary[i] = 1
    return diсtionary
dictionary = dictionary_fun()
#Функция, которая переберет словарь и выдаст часто повторяющиеся слова по значению(счету)
def common_word_fun():
    for i  in dictionary.values():
        if i == max(dictionary.values()):
            account = i
    return account
account = common_word_fun()
#Функция, которая определяет соответствующий максимальному счету слова ключ
def items_fun(dictionary,account):
    for key, value in dictionary.items():
        if value == account:
            return key
common_word = items_fun(dictionary,account)
print(f'Самое часто встречающееся слово: "{common_word}" вcтречается {account} раза')
# Напишите название файла с расширением: test.txt
# Самое длинное слово: "Умопомрачительно."
# Самое часто встречающееся слово: "baby" вcтречается 2 раза
