
# ДЗ #1
- Расширить тестовое покрытие smoke тестами на доступность микросервиса
  - добавить сервисный эндпоинт `/status` для проверки доступности микросервиса
- Использовать библиотеку fastapi-pagination для базовой пагинации в эндпоинтах, которые возвращают список объектов
- Добавить тесты на пагинацию. Тестовых данных должно быть достаточно для проверки пагинации (не менее 10)
- Проверяем:
    - ожидаемое количество объектов в ответе
    - правильное количество страниц при разных значениях size
    - возвращаются разные данные при разных значениях page


**Установка**

Клонируйте репозиторий:
```bash
git clone <URL этого репозитория>
```

Перейдите в директорию проекта:
```bash
cd <имя директории куда скачали репозиторий>
```

Установите необходимые зависимости:
```bash
pip install -r requirements.txt
```

**Запуск**

Чтобы запустить сервис, выполните команду:
```bash
uvicorn main:app --host=127.0.0.1 --port=8004 --reload
```
Проверялся запуск на windows, как на других ОС, как работает не проверял

**Тестирование**

Для запуска тестов используйте:
Перед тем как запустить тесты откройте новую console, чтобы там ввести эту команду
```bash
pytest .\tests\ -v
```
