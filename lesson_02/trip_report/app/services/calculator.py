#Расчёты по расходам. Модуль ничего не печатает — только возвращает значения.


def calculate_total(expenses):
    #Возвращает суммарные траты.
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_average(expenses):
    #Возвращает среднюю трату. На пустом списке — ValueError.
    if not expenses:
        raise ValueError("список расходов пуст")
    return calculate_total(expenses) / len(expenses)


def most_expensive_day(expenses):
    #Возвращает (номер дня, сумма) с самой большой суммой за день.

    #На пустом списке — ValueError.
    
    if not expenses:
        raise ValueError("список расходов пуст")

    totals_by_day = {}
    for expense in expenses:
        day = expense["day"]
        totals_by_day[day] = totals_by_day.get(day, 0) + expense["amount"]

    best_day = max(totals_by_day, key=totals_by_day.get)
    return best_day, totals_by_day[best_day]


def category_share(expenses, category):
    #Возвращает долю категории в общих тратах, в процентах.

    #ValueError — на пустом списке и если категории нет в данных.
    
    if not expenses:
        raise ValueError("список расходов пуст")

    total = calculate_total(expenses)
    category_total = 0
    found = False
    for expense in expenses:
        if expense["category"] == category:
            category_total += expense["amount"]
            found = True

    if not found:
        raise ValueError(f"категория «{category}» не найдена в расходах")

    return category_total / total * 100