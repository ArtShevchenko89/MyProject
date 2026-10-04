"""Функції для аналізу оцінок за 100-бальною шкалою."""

PASS_THRESHOLD = 60


def _validate(scores):
    if not scores:
        raise ValueError("Список оцінок порожній")
    for score in scores:
        if not 0 <= score <= 100:
            raise ValueError(f"Оцінка {score} поза межами 0–100")


def average(scores):
    """Середній бал."""
    _validate(scores)
    return sum(scores) / len(scores)


def median(scores):
    """Медіана оцінок."""
    _validate(scores)
    ordered = sorted(scores)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return float(ordered[middle])
    return (ordered[middle - 1] + ordered[middle]) / 2


def letter_grade(score):
    """Оцінка за шкалою ECTS."""
    _validate([score])
    scale = [(90, "A"), (82, "B"), (74, "C"), (64, "D"), (60, "E"), (35, "FX")]
    for bound, letter in scale:
        if score >= bound:
            return letter
    return "F"


def passed(score):
    """Чи зараховано дисципліну."""
    return letter_grade(score) not in ("FX", "F")


def summary(scores):
    """Підсумкова статистика групи."""
    return {
        "count": len(scores),
        "average": round(average(scores), 2),
        "median": median(scores),
        "passed": sum(1 for score in scores if passed(score)),
    }