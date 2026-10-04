from .grades import letter_grade, summary


def format_report(group, scores):
    stats = summary(scores)
    lines = [
        f"Група: {group}",
        f"Кількість студентів: {stats['count']}",
        f"Середній бал: {stats['average']}",
        f"Медіана: {stats['median']}",
        f"Зараховано: {stats['passed']} з {stats['count']}",
        "Оцінки ECTS: " + ", ".join(letter_grade(s) for s in scores),
    ]
    return "\n".join(lines)
