def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 0
    upper_bound = None
 
    while low <= high:
        iterations += 1
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid]
 
        # інакше x присутній на позиції і повертаємо його
        else:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
 
    # якщо елемент не знайдений, визначаємо верхню межу
    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]
 
    return (iterations, upper_bound)

# Приклад використання:
sorted_array = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
target_value = 0.65
result = binary_search(sorted_array, target_value)
print(result)  

# Наприклад, виведе (3, 0.7), 
# 3 - кількість ітерацій, потрібних для знаходження елемента, a
# 0.7 - "верхня межа" (найменший елемент, який є більшим або рівним заданому значенню 0.65)
