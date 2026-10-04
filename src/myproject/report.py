import os
from .grades import summary, letter_grade


def format_report(group,scores):
    stats=summary(scores)
    lines = [f"Група: {group}", f"Кількість студентів: {stats['count']}", f"Середній бал: {stats['average']}"]
    lines.append(f"Медіана: {stats['median']}")
    lines.append(f"Зараховано: {stats['passed']} з {stats['count']}")
    lines.append("Оцінки ECTS: " + ", ".join(letter_grade(s) for s in scores))
    return "\n".join(lines)