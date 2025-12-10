import pytest
from csv_processing.report_performance import PerformanceReport


def test_create_performance_report():
    """
    Test that PerformanceReport successfully creates a report.
    """
    # Mock data generator
    def data_generator():
        yield {"position": "manager", "performance": "0.9"}
        yield {"position": "developer", "performance": "0.8"}
        yield {"position": "manager", "performance": "0.95"}

    report = PerformanceReport(data_generator=data_generator())
    average_performance = report.create()

    # Convert to dictionary for easier comparison
    average_performance_dict = dict(average_performance)

    assert average_performance_dict == {
        "manager": "0.93",
        "developer": "0.80",
    }


def test_create_performance_report_missing_keys(caplog):
    """
    Test that PerformanceReport handles missing keys gracefully.
    """
    # Mock data generator
    def data_generator():
        yield {"position": "manager", "performance": "0.9"}
        yield {"position": "developer"}  # Missing 'performance', default is 0.00
        yield {"performance": "0.8"}  # Missing 'position'

    report = PerformanceReport(data_generator=data_generator())
    average_performance = report.create()

    # Convert to dictionary for easier comparison
    average_performance_dict = dict(average_performance)

    assert average_performance_dict == {"manager": "0.90", "developer": "0.00"}  # 0.9 / 1
    assert "Skipping row" in caplog.text


def test_create_performance_report_invalid_values(caplog):
    """
    Test that PerformanceReport handles invalid values gracefully.
    """
    # Mock data generator
    def data_generator():
        yield {"position": "manager", "performance": "0.9"}
        yield {"position": "developer", "performance": "invalid"}

    report = PerformanceReport(data_generator=data_generator())
    average_performance = report.create()

    # Convert to dictionary for easier comparison
    average_performance_dict = dict(average_performance)

    assert average_performance_dict == {"manager": "0.90"}
    assert "Skipping row" in caplog.text


def test_create_performance_report_no_data():
    """
    Test that PerformanceReport handles no data gracefully.
    """
    # Mock data generator
    def data_generator():
        yield from []

    report = PerformanceReport(data_generator=data_generator())
    average_performance = report.create()

    assert average_performance == []
