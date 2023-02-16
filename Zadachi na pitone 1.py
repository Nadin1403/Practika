# edibles = ["отбивные", "яйца", "пельмени", "орехи"]
# for food in edibles:
#     if food == "пельмени":
#         print("Я не ем пельмени !")
#         break
#     print("Отлично, вкусные " + food,"!")
# else:
#     print("Хорошо, что не было пельменей !")
# print("Ужин окончен !")

# edibles = ["отбивные", "яйца", "пельмени", "орехи"]
# for food in edibles:
#     if food == "пельмени":
#         print("Я не ем пельмени !")
#         continue
#     print("Отлично, вкусные " + food,"!")
# else:
#     print("Хорошо, что не было пельменей !")
# print("Ужин окончен !")

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i = i + 1

# for letter in "программист":
#     if letter == "м":
#         break
# else:
#     print("Перебор букв в слове закончен.")

# a = 8
# b = 1
# while(a>5):
#     a-=2
#     b+=a
# print(b)

# a = 1
# b = 3
# while(a!=5):
#     a+=2
#     b+=a
# print(b)

# a = 3
# b = 0
# while(a<6):
#     a+=4
#     b+=a
# print(b)

# num = int(input())
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input())
# data.sort()
# print(data)

# words = input()
# data = []
# while words != "":
#     if words not in data:
#         data.append(words)
#     words = input()
#
# for item in data:
#     print(item)


# Программа превращает введеный текст в изображение половинки елочки
count = 1
c = 0
result = []
result_2 = []
text = input('Напишите текст тут\n')

for i in text:
    c += 1
    result_2.append(str(i))
    if c == count:
        result.append(result_2)
        result_2 = []
        count += 1
        c = 0
else:
    result.append(result_2)

for branch in result:
    print(' '.join(branch))
















