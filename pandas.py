import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv('data.csv')  # Замените на ваш файл

# Вывод первых 5 строк
print(df.head())

# Простая агрегация: среднее значение по колонке 'value'
average_value = df['value'].mean()
print(f"Среднее значение: {average_value}")

