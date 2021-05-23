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
Из директории, в которой была создана копия проекта, переходим в папку my_project
```bash
cd my_project/
```
Активируем виртуальное окружение, если это еще не сделано.
```bash
source myvenv/bin/activate
```
Далее переходим в myjokes
```bash
cd myjokes/
```
Запускаем сервер
```bash
python3 manage.py runserver
```
### Использование функций сервера
#### 1. Регистрация
После того как Вы перейдете по ссылке, можно зарегистрировать  пользователя. Для этого в адресной строке нужно добавить /rest-auth/registration/. Перед нами должно появиться окно регистрации.
![aaaaaa](/screens/Снимок экрана от 2021-05-23 18-13-04.png)
#### 2. Авторизация