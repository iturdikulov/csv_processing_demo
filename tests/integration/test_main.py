from pathlib import Path
from unittest.mock import patch

import pytest
from csv_processing.main import main


def test_main_success(lazy_shared_datadir: Path, capsys):
    """
    Test that main function successfully runs and prints a report.
    """
    # Mock the command-line arguments
    with patch(
        "sys.argv",
        [
            "csv_processing_demo",
            "--files",
            str(lazy_shared_datadir / "empl_integration_01.csv"),
            "--files",
            str(lazy_shared_datadir / "empl_integration_02.csv"),
            "--files",
            str(lazy_shared_datadir / "empl_integration_03.csv"),
        ],
    ):
        main()

    # Capture the output
    captured_out = capsys.readouterr().out.lower()

    # Assert that the output contains the expected table
    assert "senior software engineer" in captured_out
    assert "financial analyst ii" in captured_out
    assert "3" in captured_out
    assert "3." in captured_out
    assert "3.1" in captured_out


def test_main_invalid_file():
    """
    Test that main function fails with invalid file path.
    """
    with patch(
        "sys.argv",
        [
            "csv_processing_demo",
            "--files",
            "invalid_file.csv",
        ],
    ):
        with pytest.raises(FileNotFoundError):
            main()


def test_main_invalid_report(lazy_shared_datadir):
    """
    Test that main function fails with invalid report type
    """
    with patch(
        "sys.argv",
        [
            "csv_processing_demo",
            "--files",
            str(lazy_shared_datadir / "empl_integration_01.csv"),
            "--report",
            "invalid_report",
        ],
    ):
        with pytest.raises(NotImplementedError):
            main()
