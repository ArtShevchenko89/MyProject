"""MyProject – облік і аналіз оцінок студентів."""

from .grades import average, letter_grade, median, passed, summary

__all__ = ["average", "median", "letter_grade", "passed", "summary"]
__version__ = "1.0.0"
