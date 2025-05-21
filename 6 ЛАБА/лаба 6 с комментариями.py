import timeit  # Модуль для измерения времени выполнения кода
import matplotlib.pyplot as plt  # Библиотека для построения графиков
import math  # Модуль math используется для вычисления факториала

# Рекурсивная реализация функции F(n) с мемоизацией
# Формула: F(n) = (-1)^n * (F(n-1)/(2n)! - 4 * F(n-2)), при F(1)=F(2)=1
def F_recursive(n, memo={}):
    if n == 1 or n == 2:  # Базовый случай по условию
        return 1
    if n not in memo:  # Вычисляем F(n), только если ещё не сохранено в memo
        factorial_2n = math.factorial(2 * n)  # Вычисление (2n)!
        # Сохраняем результат в memo, вся правая часть домножается на (-1)^n
        memo[n] = (-1 if n % 2 else 1) * (F_recursive(n - 1, memo) / factorial_2n - 4 * F_recursive(n - 2, memo))
    return memo[n]  # Возвращаем закешированное или новое значение

# Итеративная реализация функции F(n)
def F_iterative(n):
    if n == 1 or n == 2:  # Базовый случай
        return 1
    F = [0] * (n + 1)  # Инициализация списка значений
    F[1], F[2] = 1, 1  # Задание начальных условий
    for i in range(3, n + 1):  # Итерация от 3 до n
        factorial_2i = math.factorial(2 * i)  # Вычисляем (2i)!
        # Прямое применение формулы
        F[i] = (-1 if i % 2 else 1) * (F[i - 1] / factorial_2i - 4 * F[i - 2])
    return F[n]  # Возвращаем F(n)

# Функция для сравнения времени выполнения обеих реализаций
def compare_methods(max_n):
    recursive_times = []  # Время выполнения рекурсии
    iterative_times = []  # Время выполнения итерации
    results = []  # Список результатов значений

    for n in range(1, max_n + 1):  # Для каждого n от 1 до max_n
        recursive_timer = timeit.Timer(lambda: F_recursive(n))  # Таймер рекурсии
        recursive_time = recursive_timer.timeit(number=1)  # Измерение времени
        recursive_times.append(recursive_time)  # Сохраняем результат

        iterative_timer = timeit.Timer(lambda: F_iterative(n))  # Таймер итерации
        iterative_time = iterative_timer.timeit(number=1)  # Измерение времени
        iterative_times.append(iterative_time)  # Сохраняем результат

        recursive_result = F_recursive(n)  # Вычисляем F(n) рекурсивно
        iterative_result = F_iterative(n)  # Вычисляем F(n) итеративно
        results.append((n, recursive_result, iterative_result))  # Сохраняем результат

    return recursive_times, iterative_times, results  # Возвращаем списки

# Основная функция программы
def main():
    max_n = 15  # Максимальное значение n
    recursive_times, iterative_times, results = compare_methods(max_n)  # Получаем данные

    print("Таблица результатов:")  # Заголовок таблицы
    print("n | Рекурсивное значение | Итеративное значение | Время рекурсии (с) | Время итерации (с)")
    print("-" * 90)  # Разделительная линия
    for i, (n, recursive_result, iterative_result) in enumerate(results):
        # Выводим строки таблицы с результатами и временем
        print(f"{n:2d} | {recursive_result:<20.10f} | {iterative_result:<20.10f} | {recursive_times[i]:.6f} | {iterative_times[i]:.6f}")

    plt.figure(figsize=(10, 5))  # Размер графика
    plt.plot(range(1, max_n + 1), recursive_times, label='Рекурсивный метод')  # Линия рекурсии
    plt.plot(range(1, max_n + 1), iterative_times, label='Итеративный метод')  # Линия итерации
    plt.xlabel('n')  # Подпись оси X
    plt.ylabel('Время выполнения (с)')  # Подпись оси Y
    plt.title('Сравнение рекурсивного и итеративного методов')  # Заголовок графика
    plt.legend()  # Легенда графика
    plt.grid(True)  # Сетка графика
    plt.show()  # Отображение графика

# Точка входа в программу
if __name__ == "__main__":
    main()
