# Text Kit

## Назначение программы

Text Kit - набор небольших функций для работы со строками,
датами, числами и проверкой данных. Он показывает, как разложить один большой
файл на модули по темам

## Дерево проекта

text-kit/
├── app/
│ ├── init.py # делает папку пакетом app
│ ├── main.py # точка запуска: константы, main(), вызов main()
│ ├── utils/
│ │ ├── init.py
│ │ ├── text.py # clean_spaces, shorten, initials, slug
│ │ └── dates.py # parse_date, format_date, is_weekend, days_between
│ └── services/
│ ├── init.py
│ ├── statistics.py # average, median, spread, count_values
│ └── validation.py # is_email, normalize_phone, is_phone, password_problems
├── tests/
│ ├── test_text.py # тесты для app/utils/text.py
│ ├── test_dates.py # тесты для app/utils/dates.py
│ ├── test_statistics.py # тесты для app/services/statistics.py
│ └── test_validation.py # тесты для app/services/validation.py
└── README.md

## Команды запуска

Из корня проекта:

```bash
python -m app.main
python -m unittest discover -s tests -v
```

## Ожидаемый вывод

СТРОКИ
Заголовок: Отчёт за март
Коротко: Отчёт за…
Инициалы: П. И. Смирнов
Адрес страницы: otchet-za-mart

ЧИСЛА
Среднее: 4.33
Медиана: 4.5
Разброс: 2
Сколько каких: {'зачёт': 3, 'незачёт': 1}

ПРОВЕРКА ДАННЫХ
Почта 'student@college.ru': подходит
Почта 'не почта': не подходит
Телефон '8 (900) 123-45-67': +79001234567
Телефон '123': не подходит
Пароль 'Qwerty12345': подходит
Пароль 'qwerty': короче восьми символов, нет ни одной цифры, нет заглавной буквы

ДАТЫ
Начало: 02.03.2026 рабочий день
Конец: 31.03.2026 рабочий день
Дней между ними: 29

## Признак, по которому функции разделены на четыре модуля

Функции разделены по области применения:

app/utils/text.py — общие операции над строками: убрать лишние
пробелы, обрезать длинную строку, сделать инициалы, превратить заголовок
в адрес страницы

app/utils/dates.py — общие операции над датами: разобрать дату,
отформатировать её, проверить выходной, посчитать дни между датами

app/services/statistics.py — расчёты по числам и коллекциям:
среднее, медиана, разброс, подсчёт вхождений

app/services/validation.py — проверка данных: почта, телефон, пароль


