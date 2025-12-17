"""
Shared fixtures for CSV processing tests.
"""

import pytest
from pathlib import Path


@pytest.fixture
def invalid_csv_files(lazy_shared_datadir: Path) -> dict[str, Path]:
    """
    All test CSV files.
    """
    return {
        "inconsistent": lazy_shared_datadir / "inconsistent.csv",
        "no_header": lazy_shared_datadir / "no_header.csv",
    }


@pytest.fixture
def valid_csv_files(lazy_shared_datadir: Path) -> dict[str, Path]:
    """
    Only valid CSV files.
    """
    return {
        "employees1": lazy_shared_datadir / "employees1.csv",
        "employees2": lazy_shared_datadir / "employees2.csv",
    }
