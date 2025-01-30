import random
import timeit
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Середній елемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Генерація тестових даних
def generate_array(size):
    return [random.randint(-1000, 1000) for _ in range(size)]

sizes = [10_000, 50_000, 100_000, 500_000]
results = {'randomized': [], 'deterministic': []}

# Вимірювання часу
for size in sizes:
    arr = generate_array(size)
    
    # Рандомізований QuickSort
    random_time = timeit.timeit(
        lambda: randomized_quick_sort(arr.copy()), 
        number=5
    ) / 5
    
    # Детермінований QuickSort
    deterministic_time = timeit.timeit(
        lambda: deterministic_quick_sort(arr.copy()), 
        number=5
    ) / 5
    
    results['randomized'].append(random_time)
    results['deterministic'].append(deterministic_time)
    
    print(f"Розмір масиву: {size}")
    print(f"   Рандомізований QuickSort: {random_time:.4f} секунд")
    print(f"   Детермінований QuickSort: {deterministic_time:.4f} секунд\n")

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.plot(sizes, results['randomized'], marker='o', label='Рандомізований')
plt.plot(sizes, results['deterministic'], marker='x', label='Детермінований')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Розмір масиву (log scale)')
plt.ylabel('Час виконання (секунди, log scale)')
plt.title('Порівняння QuickSort алгоритмів')
plt.legend()
plt.grid(True)
plt.show()