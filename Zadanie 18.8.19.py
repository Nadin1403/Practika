count = 0
vsego_biletov = int(input('Сколько билетов Вы хотите купить? '))
for i in range(vsego_biletov):
    i += 1
    vozrast = int(input(f'Введите цифрами количество полных лет посетителя по {i} билету: '))
    if vozrast < 18:
            print('Цена билета = 0 рублей')
    elif 18 <= vozrast < 25:
            count += 990
            print('Цена билета = 990 рублей')
    else:
            count += 1390
            print('Цена билета = 1390 рублей')
if vsego_biletov > 3:
    print(f'Общая сумма без скидки = {count} рублей')
    skidka_count = count - ((count / 100) * 10)
    print(f'Итоговая сумма к оплате = {skidka_count} рублей, с учётом скидки 10 %, так как Вы регистрируете больше трёх человек.')
else:
    print(f'Итоговая сумма к оплате = {count} рублей')
