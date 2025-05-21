import timeit
import matplotlib.pyplot as plt
import math

# Рекурсивная реализация с мемоизацией
def fact(k):
    if k == 1:
        return 1
    else:
        return k * fact(k - 1)

def F_recursive(n, memo={}):
    if n == 1 or n == 2:
        return 1
    if n not in memo:
        factorial_2n = fact(2 * n)
        memo[n] = (-1 if n % 2 else 1) * (F_recursive(n - 1, memo) / factorial_2n - 4 * F_recursive(n - 2, memo))
    return memo[n]

# Итеративная реализация
def F_iterative(n):
    if n == 1 or n == 2:
        return 1
    prev2, prev1 = 1, 1
    for i in range(3, n + 1):
        sign = (-1 if i % 2 else 1)
        factorial_2i = math.factorial(2 * i)
        curr = sign * (prev1 / factorial_2i - 4 * prev2)
        prev2, prev1 = prev1, curr
    return prev1


# Сравнение времени выполнения
def compare_methods(max_n):
    recursive_times = []
    iterative_times = []
    results = []

    for n in range(1, max_n + 1):
        recursive_timer = timeit.Timer(lambda: F_recursive(n))
        recursive_time = recursive_timer.timeit(number=1)
        recursive_times.append(recursive_time)

        iterative_timer = timeit.Timer(lambda: F_iterative(n))
        iterative_time = iterative_timer.timeit(number=1)
        iterative_times.append(iterative_time)

        recursive_result = F_recursive(n)
        iterative_result = F_iterative(n)
        results.append((n, recursive_result, iterative_result))

    return recursive_times, iterative_times, results

# Главная функция
def main():
    max_n = 15
    recursive_times, iterative_times, results = compare_methods(max_n)

    print("Таблица результатов:")
    print("n | Рекурсивное значение | Итеративное значение | Время рекурсии (с) | Время итерации (с)")
    print("-" * 90)
    for i, (n, recursive_result, iterative_result) in enumerate(results):
        print(f"{n:2d} | {recursive_result:<20.10f} | {iterative_result:<20.10f} | {recursive_times[i]:.6f} | {iterative_times[i]:.6f}")

    plt.figure(figsize=(10, 5))
    plt.plot(range(1, max_n + 1), recursive_times, label='Рекурсивный метод')
    plt.plot(range(1, max_n + 1), iterative_times, label='Итеративный метод')
    plt.xlabel('n')
    plt.ylabel('Время выполнения (с)')
    plt.title('Сравнение рекурсивного и итеративного методов')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
