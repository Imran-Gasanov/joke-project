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
REQUEST

endpoint: /rest-auth/registration/

method: POST

Body:
```html
{
    "username": "Shrek",
    "email": "shrek@mail.com",
    "password1": "shrekl0vef1ona",
    "password2":  "shrekl0vef1ona"
}
```
RESPONSE

Status Code: 200 Ok

Str: "Joke"![Регистрация](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/1.png)
#### 2. Авторизация
Авторизация проходит аналогично, только теперь к адресу добавляем /rest-auth/login/. Заполняем поля и снова получаем ключ.
![Авторизация](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/2.png)
#### 3. Генерация шутки
REQUEST

endpoint: /generate/

method: GET

Headers: Authorization: Token keyToken

RESPONSE

Status Code: 200 Ok

Str: "Joke"
![Генерация](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/3.png)
#### 4. Создание шутки
Создаем "POST" запрос /jokes/, добавляем в Headers ключ пользователя также как и в генерации шутки, а в "Body" записываем нашу шутку.
![Создание](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/4.png)
#### 5. Просмотр шуток
Создаем "POST" запрос /jokes/, добавляем в Headers ключ пользователя. Вернется список наших шуток, если ввести /jokes/id/, вернется только одна шутка по id.(контент второй шутки изменен, потому что скрин из будущего)
![Просмотрвсех](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/5.png)
![Просмотродной](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/6.png)
#### 6. Удаление шутки
Создаем "DELETE" запрос /jokes/, добавляем в Headers ключ пользователя.
![Удаление](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/7.png)
Проверяем список наших шуток, видим, что шутка удалена.
![Просмотрвсех](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/8.png)
#### 7. Изменение шутки
Создаем "PUT" запрос /jokes/id/, добавляем в Headers ключ пользователя, в "Body" записываем контент измененной шутки.
![Изменение](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/10.png)
Снова проверяем список шуток, видим, что шутка изменена.
![Просмотрвсех](https://github.com/Imran-Gasanov/joke-project/raw/master/screens/11.png)
