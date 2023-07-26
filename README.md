# Автоматизация получения ежедневной бесплатной электронной книги от Packtpub

> :warning: **Disclaimer**\
> Материал представлен исключительно в ознакомительных целях.\
> Я не призываю никого использовать данную автоматизацию на практике и не несу ответственности за возможную блокировку личного акккаунта Packtpub и иные последствия, вызванные ее использованием.

## Описание проекта
С недавних пор я открыл для себя сервис [Packtpub](https://www.packtpub.com/) (об издательстве знал до этого), где можно не только читать электронные версии книг издательства Packt, но и проходить различные online-курсы.

С удовольствием для себя я отметил и возможность ежедневно добавлять на аккаунт одну бесплатную книгу. В большинстве своем, конечно, это либо нечто морально устаревшее, либо не подходящее лично мне по профилю, но иногда попадаются и книги, которые я был бы рад иметь под рукой.

С тех пор я ежедневно заходил на сайт и выполнял рутинные действия, со временем накопив на Packtpub приличную библиотеку, в которой стало сложно ориентироваться со временем.

В итоге я решил устранить две проблемы:
- избавиться от рутинного процесса посещения сайта;
- автоматически добавлять минимальную информацию о добавленной книге в соответствующую заметку в Obsidian (он хранит заметки локально в виде markdown-файлов). Существующий список книг существует в виде таблицы из трех полей - этим и продиктован специфический формат вывода.

Для решения задачи я впервые для себя применил библиотеку веб-парсинга pyppeteer и написал python-скрипт для аутентификации на сайте, перехода на страницу раздачи и сбор базовой информации о добавленной книге (название и ссылка).

## Содержимое репозитория
|Файл|Описание|
|-|-|
|[parser_script.py](parser_script.py)|Python-скрипт парсера, выполняющего необходимые действия.|
|[packt_parser_job.sh](packt_parser_job.sh)|Bash-скрипт, запускающий скрипт парсера.</br>Поскольку проект создавался в виртуальной среде python, bash-скрипт содержит и команду для ее активации.</br>Для автоматизации данный скрипт остается только запланировать в crontab.|

## Дальнейшие шаги
- На текущий момент скрипт только выводит информацию о добавленной книге, но не сохраняет ее и не отправляет мне. В планах настроить отправку этой информации мне на почту, откуда ее будет легко скопировать и вставить в нужный файл.
- Также планирую развернуть Airflow для личных нужд и передать управление автоматизацией ему. Перед этим протестирую сервис [ScrapeOps](https://scrapeops.io), используемый как раз для оркестрации парсеров.