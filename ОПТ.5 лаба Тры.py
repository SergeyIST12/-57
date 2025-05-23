import timeit
from itertools import permutations

# Часть 1: Формирование всех возможных вариантов обхода точек
def algorithmic_method(points):
    """Алгоритмический метод формирования всех перестановок"""
    result = [[]]
    for _ in range(len(points)):
        temp = []
        for path in result:
            for point in points:
                if point not in path:
                    temp.append(path + [point])
        result = temp
    return result

def python_method(points):
    """Метод с использованием itertools.permutations"""
    return list(permutations(points))

# Часть 2: Ограничения и целевая функция
def calculate_distance(path):
    """Вычисляем суммарное расстояние для заданного пути"""
    distance = 0
    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]
        distance += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

def optimized_method_compact(points, min_distance, max_total_distance):
    """
    Компактная версия оптимизированного метода с ограничениями:
    1) Минимальное расстояние между соседними точками
    2) Максимальная суммарная длина пути
    """
    return [
        (path, calculate_distance(path))
        for path in python_method(points)
        if all(
            ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 >= min_distance
            for (x1, y1), (x2, y2) in zip(path, path[1:])
        )
        and calculate_distance(path) <= max_total_distance
    ]

# Ввод данных
K = 4  # Количество точек
points = [(1, 1), (2, 3), (3, 2), (4, 4)]  # Координаты точек

# Часть 1: Сравнение времени выполнения двух методов
print("Часть 1: Все возможные варианты обхода точек")
all_paths_algo = algorithmic_method(points)
all_paths_python = python_method(points)

print(f"Алгоритмический метод: {len(all_paths_algo)} путей")
for path in all_paths_algo:
    print(path)
print(f"Метод с itertools.permutations: {len(all_paths_python)} путей")
for path in all_paths_python:
    print(path)

time_algo = timeit.timeit(lambda: algorithmic_method(points), number=1000)
time_python = timeit.timeit(lambda: python_method(points), number=1000)

print("\nСравнение времени выполнения:")
print(f"Алгоритмический метод: {time_algo:.6f} секунд")
print(f"Метод с itertools.permutations: {time_python:.6f} секунд")
print("Быстрее -", "алгоритмический метод" if time_algo < time_python else "метод itertools.permutations")

# Часть 2: Оптимизация с ограничениями
min_distance = 1.5  # Минимальное расстояние между соседними точками
max_total_distance = 10.0  # Максимальная суммарная длина пути

optimal_paths = optimized_method_compact(points, min_distance, max_total_distance)
print("\nЧасть 2: Оптимизированные пути с ограничениями")
if optimal_paths:
    print(f"Найдено {len(optimal_paths)} оптимальных путей:")
    for i, (path, distance) in enumerate(optimal_paths, 1):
        print(f"{i}) Путь: {path}, Длина: {distance:.2f}")
else:
    print("Оптимальных путей не найдено.")
