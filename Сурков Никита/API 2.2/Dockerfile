FROM ubuntu:20.04

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y python3 python3-pip build-essential default-libmysqlclient-dev python3-dev pkg-config

# Копируем все файлы проекта в контейнер
COPY . .

# Устанавливаем все зависимости, указанные в requirements.txt
RUN pip install -r requirements.txt

# Задаем переменную среды для указания точки входа для Flask-приложения
ENV FLASK_APP=main

# Открываем порт 8000 для внешнего доступа
EXPOSE 8000

# Запускаем Flask-приложение на хосте 0.0.0.0 и порту 8000
CMD flask run --host 0.0.0.0 --port 8000

