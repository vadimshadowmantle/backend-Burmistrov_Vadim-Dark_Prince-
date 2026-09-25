#Оформление отчёта. Только представление — расчётов здесь нет.

from rich.console import Console
from rich.table import Table


def format_report(expenses, total, average, best_day, best_sum, food_share, housing_share):
    #Собирает и печатает отчёт таблицей Rich.
    console = Console()

    summary = Table(title="ОТЧЁТ ПО ПОЕЗДКЕ", show_header=True, header_style="bold")
    summary.add_column("Показатель", style="cyan")
    summary.add_column("Значение", justify="right", style="green")

    summary.add_row("Записей", str(len(expenses)))
    summary.add_row("Всего потрачено", f"{total} ₽")
    summary.add_row("Средняя трата", f"{average:.2f} ₽")
    summary.add_row("Самый дорогой день", f"день {best_day}, {best_sum} ₽")
    summary.add_row("Доля «еда»", f"{food_share:.2f} %")
    summary.add_row("Доля «жильё»", f"{housing_share:.2f} %")

    console.print(summary)