# Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления
# данной функции рекурсивно и итерационно. Определить границы применимости рекурсивного и итерационного подхода.
# Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
# Вариант №7
# F(1) = 1; G(1) = 1; F(n) = 3*F(n–1) – 3*G(n–1), G(n) = F(n–1) + 2*G(n–1), при n >=2

import time
import matplotlib.pyplot as plt

# -----Рекурсия-----
def rec_f(n):
    if n == 2:
        return 1
    else:
        return 3 * rec_f(n - 1) - 3 * rec_g(n - 1)

def rec_g(n):
    if n == 2:
        return 1
    else:
        return rec_f(n - 1) + 2 * rec_g(n - 1)

# -----Итерация-----
def iter_f(n):
    gn = [1] * (n + 1)
    fn = [1] * (n + 1)
    for m in range(3, n + 1):
        fn[m] = 3 * fn[m - 1] - 3 * gn[m - 1]
        gn[m] = fn[m - 1] + 2 * gn[m - 1]
    return fn[n]

try:
    n = int(input('Введите натуральное число n >= 2: '))
    while n < 2:  # Ошибка в случае введения не натурального числа
        n = input('Вы ввели число меньше 2. В условии указано, что число должно быть больше или равно 2.')

    k = 1
    if int(n) > 25:
        k = int(input('Число n > 25. Хотите продолжить? Это может занять существенное время. (Да - 1 / Нет - 0): '))
    while k != 0 and k != 1:
        k = int(input('Вы ввели не 1 и не 0. Введите 1, чтобы продолжить или 0, чтобы завершить программу: '))

    # -----Создание списков для построения таблицы-----
    if k == 1:
        rec_times = []
        rec_values = []
        iter_times = []
        iter_values = []
        n_values = list(range(2, int(n) + 1))

        # -----Заполнение списков данными-----
        for n in n_values:
            start = time.time()
            rec_values.append(rec_f(n))
            end = time.time()
            rec_times.append(end - start)

            start = time.time()
            iter_values.append(iter_f(n))
            end = time.time()
            iter_times.append(end - start)

        # -----Создание и заполнение последующей таблицы-----
        table_data = []
        for i, n in enumerate(n_values):
            table_data.append([n, rec_times[i], iter_times[i], rec_values[i], iter_values[i]])

        # -----Вывод таблицы-----
        print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии', 'Значение итерации'))
        print('-' * 104)
        for data in table_data:
            print('{:<7}|{:<25}|{:<25}|{:<25}|{:<25}'.format(data[0], data[1], data[2], data[3], data[4]))

        # -----Вывод графиков-----
        plt.plot(n_values, iter_times, label='Итерация')
        plt.plot(n_values, rec_times, label='Рекурсия')
        plt.xlabel('n')
        plt.ylabel('Время (с)')
        plt.title('Сравнение рекурсивного и итерационного подхода')
        plt.legend()
        plt.show()

    print('Работа программы завершена.')
except ValueError:
    print('Вы ввели число, не следуя условиям. Перезапустите программу и введите число, следуя инструкциям.')

except RecursionError:
    print('Вы превысили относительную максимальную глубину рекурсии.')
