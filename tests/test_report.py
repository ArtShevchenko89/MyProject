from myproject.report import format_report


def test_format_report_contains_statistics():
    report = format_report("ІПЗ-41", [72, 85, 90, 64, 58, 95])
    assert "Група: ІПЗ-41" in report
    assert "Середній бал: 77.33" in report
    assert "Зараховано: 5 з 6" in report
    assert report.endswith("Оцінки ECTS: D, B, A, D, FX, A")
