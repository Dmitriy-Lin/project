# Friends
Проект социальной сети.
# Установка
- Установите инструмент virtualenv при помощи pip
>$ pip install virtualenv
- Создайте новую виртуальную среду Python командой:
>$ python3 -m venv env
- Активируйте виртуальную среду Python:
>$ source env/bin/activate
#### Клонируйте репозиторий в нужный Вам каталог 
>git clone https://github.com/Dmitriy-Lin/project.git
- В Вашей папке со скопированным проектом найдите файл requirements.txt и запустите его командой:  
>$ pip install -r requirements.txt
###### это установит все необходимые пакеты и зависимости для работы проекта
- Для работы чата необходимо установить redis-server выполните команду:
>$sudo apt-get install redis-server
#### Установите СУБД PostgreSQL выполнив команду:
>$sudo apt-get install wget ca-certificates
>###### $wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
>###### $sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
>###### $sudo apt-get update
>###### $sudo apt-get install postgresql postgresql-contrib
- создайте базу данных, для этого воспользуйтесь документацией:
>https://postgrespro.ru/docs
#### После установки необходимых компонентов можно перейти к настроке проекта
- в папке friends найдите файл settings.py
- в строке DATABASES установите имя пользователя и пароль для доступа к Вашей базе данных
>- 'ENGINE': 'django.db.backends.postgresql',
>- 'USER': 'user',
>- 'PASSWORD': 'password',
>- 'NAME': 'friends',
- так же для работы системы отправки сообщений для верификации аккаунта установите настройки Вашего почтового сервера, пример приведен для https://www.mailgun.com:
>- EMAIL_HOST = 'smtp.mailgun.org'
>- EMAIL_PORT = 587
>- EMAIL_USE_TLS = True
>- EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
>- EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
>- DEFAULT_FROM_EMAIL = 'admin@friends.com'
### Запуск
#### После настройки, для запуска локального сервера, для начала проведите миграции в базу данных выполнив команды:
>- $python3 manage.py makemigrations
>- $python3 manage.py migrate

*Operations to perform:*<br/>
*Apply all migrations: books*<br/> 
*Running migrations:*<br/>
*Rendering model states... DONE*<br/>
*Applying books.0003_auto... OK*<br/>

#### После проведения миграций можно запустить сервер командой:
> $python3 manage.py runserver
#### Если все прошло успешно Вы увидите в консоли следующее сообщение
*Watching for file changes with StatReloader*<br/>
*Performing system checks...*<br/>
**<br/>
*System check identified no issues (0 silenced).*<br/>
*October 18, 2019 - 17:42:23*<br/>
*Django version 2.2.6, using settings 'friends.settings'*<br/>
*Starting ASGI/Channels version 2.3.0 development server at http://127.0.0.1:8000/*<br/>
*Quit the server with CONTROL-C.*<br/>
#### Поздравляю сервер успешно запущен теперь можете перейти по адресу http://127.0.0.1:8000 и начать пользоваться сайтом
#### В папке static находится файл *friends.json* который содержит тестовый набор пользователей, для заполнения БД введите комманду:
>$python3 manage.py seeds

