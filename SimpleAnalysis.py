import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генерация данных

data = [random.randint(-10000, 10000) for _ in range(1000)]

# Создание Series

series = pd.Series(data)

# Статистические характеристики

min_value = series.min()
max_value = series.max()
sum_value = series.sum()
std_value = series.std()
duplicates_count = series.duplicated().sum()

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Сумма значений:", sum_value)
print("Количество повторов:", duplicates_count)
print("Среднеквадратическое отклонение:", std_value)

# Линейный график

plt.figure(figsize=(10, 5))
plt.plot(series)
plt.title("Линейный график исходных данных")
plt.grid(True)
plt.savefig("line_graph.png")
plt.show()

# Гистограмма

rounded_series = series.round(-2)

plt.figure(figsize=(10, 5))
plt.hist(rounded_series, bins=30)
plt.title("Гистограмма распределения данных")
plt.grid(True)
plt.savefig("histogram.png")
plt.show()

# Создание DataFrame

df = pd.DataFrame({
"Original": series,
"Ascending": sorted(series),
"Descending": sorted(series, reverse=True)
})

print(df.head())

# График отсортированных данных

plt.figure(figsize=(10, 5))
plt.plot(df["Ascending"], label="По возрастанию")
plt.plot(df["Descending"], label="По убыванию")
plt.title("Сравнение отсортированных данных")
plt.legend()
plt.grid(True)
plt.savefig("sorted_graph.png")
plt.show()
