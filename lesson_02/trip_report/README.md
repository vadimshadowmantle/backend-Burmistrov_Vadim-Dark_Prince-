**Бурмистров Вадим Александрович, группа 11/1-РПО-26/1.** 

## Окружение

- Python 3.12.x
- Интерпретатор: `/home/user/trip-report/.venv/bin/python`
  (свой вывод `python -c "import sys; print(sys.executable)"`)

## Структура проекта

app/__init__.py                пакет приложения
app/main.py                    точка входа: данные, вызовы расчётов, печать отчёта
app/services/calculator.py     только расчёты, ничего не печатает
app/utils/formatter.py         только оформление отчёта таблицей Rich
tests/test_calculator.py       тесты расчётов
requirements.txt               зависимости проекта
README.md                      этот файл

## Установка и запуск

### Windows 

py -m venv .venv 

.venv\Scripts\activate

pip install -r requirements.txt

python -m app.main


### macOS

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python -m app.main


Если PowerShell не даёт активировать окружение попробуйте запустить его от имени админа



























































































#Тёмный принц (Ыа-Ыа)