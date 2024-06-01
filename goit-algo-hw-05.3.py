import timeit

# Алгоритм Кнута-Морріса-Пратта (KMP)
def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


# Алгоритм Боєра-Мура
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0: return 0
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1


# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


# Завантажуємо текстові файли
with open(r'C:\Users\Yulii\Projects\!Repository\goit-algo-hw-05\стаття 1.txt', 'r', encoding='windows-1251') as f:
    text1 = f.read()

with open(r'C:\Users\Yulii\Projects\!Repository\goit-algo-hw-05\стаття 2.txt', 'r', encoding='windows-1251') as f:
    text2 = f.read()


# Вибираємо підрядки
existing_substring1 = text1[100:110]
non_existing_substring1 = "Чорнобривців насіяла мати"
existing_substring2 = text2[200:210]
non_existing_substring2 = "У моїм світанковім краю"

# Функція для вимірювання часу виконання
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1000)

# Вимірювання часу для статті 1
kmp_time_exist1 = measure_time(kmp_search, text1, existing_substring1)
kmp_time_non_exist1 = measure_time(kmp_search, text1, non_existing_substring1)

bm_time_exist1 = measure_time(boyer_moore, text1, existing_substring1)
bm_time_non_exist1 = measure_time(boyer_moore, text1, non_existing_substring1)

rk_time_exist1 = measure_time(rabin_karp, text1, existing_substring1)
rk_time_non_exist1 = measure_time(rabin_karp, text1, non_existing_substring1)

# Вимірювання часу для статті 2
kmp_time_exist2 = measure_time(kmp_search, text2, existing_substring2)
kmp_time_non_exist2 = measure_time(kmp_search, text2, non_existing_substring2)

bm_time_exist2 = measure_time(boyer_moore, text2, existing_substring2)
bm_time_non_exist2 = measure_time(boyer_moore, text2, non_existing_substring2)

rk_time_exist2 = measure_time(rabin_karp, text2, existing_substring2)
rk_time_non_exist2 = measure_time(rabin_karp, text2, non_existing_substring2)

# Результати
results = {
    "article1": {
        "KMP": {"existing": kmp_time_exist1, "non-existing": kmp_time_non_exist1},
        "Boyer-Moore": {"existing": bm_time_exist1, "non-existing": bm_time_non_exist1},
        "Rabin-Karp": {"existing": rk_time_exist1, "non-existing": rk_time_non_exist1},
    },
    "article2": {
        "KMP": {"existing": kmp_time_exist2, "non-existing": kmp_time_non_exist2},
        "Boyer-Moore": {"existing": bm_time_exist2, "non-existing": bm_time_non_exist2},
        "Rabin-Karp": {"existing": rk_time_exist2, "non-existing": rk_time_non_exist2},
    }
}

# Визначення найшвидшого алгоритму
def find_fastest(results):
    fastest = {}
    for article, times in results.items():
        fastest[article] = {"existing": min(times, key=lambda x: times[x]["existing"]),
                            "non-existing": min(times, key=lambda x: times[x]["non-existing"])}
    return fastest

fastest_algorithms = find_fastest(results)

print("Результати:", results)
print("Найшвидші алгоритми:", fastest_algorithms)


# Висновки 
"""
Висновки 

Стаття 1 
KMP:
- Існуючий підрядок: 0.013187999997171573
- Неіснуючий підрядок: 1.3771836000087205
Boyer-Moore:
- Існуючий підрядок: 0.003606100013712421
- Неіснуючий підрядок: 0.1633566999953473
Rabin-Karp:
- Існуючий підрядок: 0.016879100003279746
- Неіснуючий підрядок: 1.901284100007615

Стаття 2
KMP:
- Існуючий підрядок: 0.02433990000281483
- Неіснуючий підрядок: 2.008207399994717
Boyer-Moore:
- Існуючий підрядок: 0.005767699985881336
- Неіснуючий підрядок: 0.27403770000091754
Rabin-Karp:
- Існуючий підрядок: 0.03289109999604989
- Неіснуючий підрядок: 2.852887000000919

Найшвидші алгоритми для кожного тексту:
  Стаття 1: Boyer-Moore
    На існуючих даних: Boyer-Moore виявився приблизно на 72.57% швидшим за KMP та на 89.72% швидшим за Rabin-Karp.
    На неіснуючих даних: Boyer-Moore виявився приблизно на 88.91% швидшим за KMP та на 91.42% швидшим за Rabin-Karp.
  Стаття 2: Boyer-Moore
    На існуючих даних: Boyer-Moore виявився приблизно на 76.35% швидшим за KMP та на 88.49% швидшим за Rabin-Karp.
    На неіснуючих даних: Boyer-Moore виявився приблизно на 91.64% швидшим за KMP та на 90.38% швидшим за Rabin-Karp.

Загальний найшвидший алгоритм для обох текстів: Boyer-Moore

"""
