A = {1, 2, 3, 4}
B = {-11, 1, -9, 3, "строка", 0.46, 12, 2, 38, "не число", 4, "hello there", }
C = {1, 5, "восемь", "строка", 4, -3, "матрица"}

# Пересечение множеств:
print(A.intersection(B))
print(A.intersection(C))
print(B & C)
print(A & B & C)

# Обьединение множеств:
print(A.union(B))
print(A.union(C))
print(B.union(C))
print(A | B | C)

# Вычитание множеств:
print(A - B)
print(B - A)
print(C - A)
print(C - B)
print(C - A - B)
print(B - C - A)
print(B - C)
print()
print()
# Симметричная разность:
print(A ^ B)
print(B ^ A)
print(C ^ B)
print(C ^ A)
# Элементы, входящие во все три множества (В данном лучае это
# 1 и 4) входят в симметричную разность, а повторяющиеся только в двух множествах - нет.
# Это из - за последовательности выполнения операций происходит? Результат одинаковый
# вне зависимости от наличия скобок.
print(C ^ B ^ A)
print((C ^ B) ^ A)
print(C ^ (B ^ A))

# Сравнение:
print(A < B)
print(B < C)
print(A != B, B != C)
print(B == C)

