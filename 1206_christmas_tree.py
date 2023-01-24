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
