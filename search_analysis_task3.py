import timeit

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def kmp_search(text, pattern):
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
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp_search(text, pattern):
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(M-1):
        h = (h * d) % q
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            j += 1
            if j == M:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return -1

def boyer_moore_search(text, pattern):
    def bad_char_heuristic(string, size):
        bad_char = [-1] * 65536
        for i in range(size):
            bad_char[ord(string[i])] = i
        return bad_char
    m = len(pattern)
    n = len(text)
    bad_char = bad_char_heuristic(pattern, m)
    s = 0
    while(s <= n - m):
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1

import timeit

def measure_performance(text, pattern, algorithm):
    setup_code = f"from __main__ import {algorithm.__name__} as algorithm, text, pattern"
    stmt = "algorithm(text, pattern)"
    times = timeit.repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    return min(times)

texts = [
    ("article1.txt", "алгоритмів у бібліотеках", "непідтверджені інформації"),
    ("article2.txt", "рекомендаційної системи", "загублених технологій")
]

algorithms = [kmp_search, rabin_karp_search, boyer_moore_search]

results = {}
for file_name, existing_substr, fictional_substr in texts:
    text = load_text(file_name)
    for pattern, pattern_type in [(existing_substr, "existing"), (fictional_substr, "fictional")]:
        for algo in algorithms:
            result_key = f"{file_name}, Pattern '{pattern_type}' using {algo.__name__}"
            performance = measure_performance(text, pattern, algo)
            results[result_key] = performance

# Вивід результатів
for result in results:
    print(f"{result}: {results[result]:.6f} seconds")

# Визначення найшвидшого алгоритму для кожного тексту
for file_name, _, _ in texts:
    fastest_time = float('inf')
    fastest_algo = None
    for algo in algorithms:
        result_key = f"{file_name}, Pattern 'existing' using {algo.__name__}"
        if results[result_key] < fastest_time:
            fastest_time = results[result_key]
            fastest_algo = algo.__name__
    print(f"Fastest algorithm for {file_name} is {fastest_algo} with time {fastest_time:.6f} seconds")
