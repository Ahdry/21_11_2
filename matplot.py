import matplotlib.pyplot as plt

# Данные для графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.savefig('plot.png')  # Сохранение графика в файл
plt.show()  # Отображение графика