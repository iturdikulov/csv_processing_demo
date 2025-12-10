import pytest
from pathlib import Path
from csv_processing.csv_loader import CSVLoader


def test_load_single_file(lazy_shared_datadir: Path):
    """
    Test that CSVLoader successfully loads a single valid CSV files.
    """

    file_1: Path = lazy_shared_datadir / "employees1.csv"
    file_2: str = str(lazy_shared_datadir / "employees2.csv")

    for file in [file_1, file_2]:
        loader = CSVLoader(files=[file])
        rows = list(loader.load())
        assert len(rows) > 0


def test_load_multiple_files(lazy_shared_datadir: Path):
    """
    Test that CSVLoader successfully loads a multiple valid CSV files.
    """

    file_1: Path = lazy_shared_datadir / "employees1.csv"
    file_2: str = str(lazy_shared_datadir / "employees2.csv")

    loader = CSVLoader(files=[file_1, file_2])
    rows = list(loader.load())
    assert len(rows) > 0


def test_load_file_not_found():
    """
    Test that CSVLoader raises FileNotFoundError for a non-existent file.
    """
    loader = CSVLoader(files=["/tmp/non_existent_file.csv"])
    with pytest.raises(FileNotFoundError):
        list(loader.load())


def test_load_inconsistent_csv(lazy_shared_datadir: Path):
    """
    Test that CSVLoader raises ValueError for an CSV file with inconsistent rows.
    """
    csv_file: Path = lazy_shared_datadir / "inconsistent.csv"

    loader = CSVLoader(files=[csv_file])
    with pytest.raises(ValueError):
        list(loader.load())
