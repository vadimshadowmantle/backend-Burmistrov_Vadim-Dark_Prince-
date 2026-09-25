#Точка входа: данные, вызовы расчётов, вывод отчёта.

from app.services.calculator import (
    calculate_total,
    calculate_average,
    most_expensive_day,
    category_share,
)
from app.utils.formatter import format_report

EXPENSES = [
    {"day": 1, "category": "еда", "amount": 540},
    {"day": 1, "category": "транспорт", "amount": 260},
    {"day": 1, "category": "жильё", "amount": 1800},
    {"day": 2, "category": "еда", "amount": 720},
    {"day": 2, "category": "транспорт", "amount": 180},
    {"day": 2, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 430},
    {"day": 3, "category": "транспорт", "amount": 95},
    {"day": 3, "category": "жильё", "amount": 1800},
    {"day": 3, "category": "еда", "amount": 275},
]


def main():
    total = calculate_total(EXPENSES)
    average = calculate_average(EXPENSES)
    best_day, best_sum = most_expensive_day(EXPENSES)
    food_share = category_share(EXPENSES, "еда")
    housing_share = category_share(EXPENSES, "жильё")

    format_report(
        EXPENSES, total, average, best_day, best_sum, food_share, housing_share
    )


if __name__ == "__main__":
    main()