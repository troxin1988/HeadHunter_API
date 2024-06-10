<h1 align="center">Привет, я - <a href="https://t.me/anton_pashinov" target="_blank">Антон</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Это парсер вакансий через API hh.ru </h3>

Программа, которая получает информацию о вакансиях с платформы hh.ru в России,
Сохраняет ее в базу данных SQL

_При запуске программы пользователю предлагается загрузить базу из hh.ru, либо воспользоваться имеющейся.
Если пользователь выбрал загрузку происходит процесс загрузки с API по каждой выбранной компании.
После загрузки всех элементов, они сохраняются в базу_

Следующим этапом наступает вывод информации из базы по определенным критериям:
1. Получить список всех компаний и количество вакансий у каждой компании
2. Получить список всех вакансий
3. Получить среднюю зарплату по вакансиям
4. Получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
5. Получить список всех вакансий по ключевому слову

<h3>Установка:</h3>
<code>git clone https://github.com/troxin1988/hhru.git</code></br>
<code>cd hhru</code></br>
<code>poetry shell</code></br>
<code>poetry install</code>

<h3>Настройка:</h3>
В файле settings.ini лежат настройки для подключения к SQL-серверу
Так же в блоке [CompanyID] расположены id различных компаний, по которым будут загружаться вакансии

<h3>Запуск:</h3>
<code>python3 main.py</code>
