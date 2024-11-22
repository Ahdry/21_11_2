import requests

# Отправка GET запроса
response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()  # Получение данных в формате JSON

# Выводим первые 5 постов
for post in data[:5]:
    print(f"Title: {post['title']}\nBody: {post['body']}\n")
