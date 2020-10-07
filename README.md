Проект представляет собой API для персонализированного сервиса task manager.
Реализован с помощью Django, Django Rest Framework.

Документация доступна после разворачивания проекта по ссылке:\
`/api/docs/` или в директории проекта `/docs/Task Manager API.pdf`
 

**ВАЖНО**: обязательно измените файл `.env.prod` и `.env.prod.db` для передачи в качестве переменных среды нужных параметров
перед применением в бою.

Проект подготовлен для deploy с помощью Docker. Для этого выполните действия:\
1. Сборка обзазов и запуск контейнеров:\
`docker-compose -f docker-compose.prod.yml up -d --build`\
2. Миграция в БД:\
`docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`\
3. Сборка static файлов для документации:\
`docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`\

C API реализована авторизация в системе по токену. Для его получения отправьте POST запрос с параметрами `username` и 
`password` на `/api/login/`. Результатом будет токен, который надо установить в header запроса при использовании
API:
`Authorization: Token <token>` 

Для регистрации пользователя отправьте POST запрос с параметрами `username` и 
`password` на `/api/register/`. Результатом будет токен.

В проекте реализована фильтрация задач пользователя по полям "Статус", "Дата окончания".
Для этого при GET-запросе задач неодходимо указать GET-параметры `status` и `expected_dead_line`. 
Реализовано с помощью django-filters.

В проекте реализована история задач с помощью django-simple-history.
