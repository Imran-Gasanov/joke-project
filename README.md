# REST-сервис
## Установка
Сначала создайте папку, в которой будет находиться проект.
```bash
mkdir my_project
```
Теперь нужно создать виртуальное окружение.
```bash
python3 -m venv myvenv
```
Далее, клонируем репозиторий в созданную директорию с помощью git clone. Для того, чтобы приложение работало на Вашем устройстве, необходимо установить те же версии библиотек, которые использовались для его создания. В файле requirements.txt содержатся все необходимые зависимости, запустим виртуальное окружение и установим их.
```bash
source myvenv/bin/activate
pip install -r requirements.txt
```
Теперь проект можно запускать.

## Применение
### Запуск сервера
Из директории, в которой была создана копия проекта, переходим в папку my_project.
```bash
cd my_project/
```
Активируем виртуальное окружение, если это еще не сделано.
```bash
source myvenv/bin/activate
```
Далее переходим в myjokes.
```bash
cd myjokes/
```
Запускаем сервер.
```bash
python manage.py runserver
```
### Использование функций сервера
Чтобы продемонстрировать функционал приложения я воспользуюсь программой "Postman".
#### 1. Регистрация
##### REQUEST

endpoint: /rest-auth/registration/

method: POST

Body:
```html
{
    "username": str,
    "email": str,
    "password1": str,
    "password2":  str
}
```
##### RESPONSE

Status Code: 201 Created
```html
{
    key: str
}
```
![Регистрация](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/1.png)
#### 2. Авторизация
##### REQUEST

endpoint: /rest-auth/login/

method: POST

Body:
```html
{
    "username": str,
    "password": str
}
```
##### RESPONSE

Status Code: 201 Created
```html
{
    key: str
}
```
Авторизация проходит аналогично, только теперь к адресу добавляем /rest-auth/login/. Заполняем поля и снова получаем ключ.
![Авторизация](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/2.png)
#### 3. Генерация шутки
###### REQUEST

endpoint: /generate/

method: GET

Headers: Authorization: Token keyToken

##### RESPONSE

Status Code: 200 Ok

Str: "Joke"
![Генерация](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/3.png)
#### 4. Создание шутки
###### REQUEST

endpoint: /generate/

method: POST

Headers: Authorization: Token keyToken

Body:
```html
{
    "content": str
}
```
##### RESPONSE

Status Code: 200 Ok
```html
{
    "url": str,
    "user": {
        "url": str,
        "username": str,
        "email": str,
        "is_staff": false
    },
    "content": str
}
```
![Создание](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/4.png)
#### 5. Просмотр шуток
###### REQUEST

endpoint: /generate/

method: GET

Headers: Authorization: Token keyToken

Body:
```html
{
    "content": str
}
```
##### RESPONSE

Status Code: 200 Ok
```html
{
    "url": str,
    "user": {
        "url": str,
        "username": str,
        "email": str,
        "is_staff": false
    },
    "content": str
}
```
![Просмотрвсех](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/5.png)
Для просмотра одной шутки в endpoint нужно добавить id шутки
![Просмотродной](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/6.png)
#### 6. Удаление шутки
###### REQUEST

endpoint: /jokes/id/

method: DELETE

Headers: Authorization: Token keyToken

##### RESPONSE

Status Code: 204 No Content
![Удаление](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/7.png)
Проверяем список наших шуток, видим, что шутка удалена.
![Просмотрвсех](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/8.png)
#### 7. Изменение шутки
###### REQUEST

endpoint: /jokes/id/

method: PUT

Headers: Authorization: Token keyToken

Body:
```html
{
    "content": str
}
```
##### RESPONSE

Status Code: 200 OK
```html
{
    "url": str,
    "user": {
        "url": str,
        "username": str,
        "email": str,
        "is_staff": false
    },
    "content": str
}
```
![Изменение](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/9.png)
Снова проверяем список шуток, видим, что шутка изменена.
![Просмотрвсех](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/10.png)
