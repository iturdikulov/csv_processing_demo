import pytest
from pathlib import Path
from csv_processing.csv_loader import CSVLoader

FILE_PATH_TYPES = ["Path", "str"]


@pytest.mark.parametrize("file_path_type", FILE_PATH_TYPES)
def test_load_single_file(
    valid_csv_files: dict[str, Path],
    invalid_csv_files: dict[str, Path],
    file_path_type: str,
):
    def verify_single_file(file: Path | str, file_path_type: str):
        """
        Test that CSVLoader successfully loads all CSV files variants.

        TODO: maybe it's overkill to allow str path type, we can simplify
        tests/logic, but this require some CSVLoader changes.
        """
        files = [file] if file_path_type == "Path" else [str(file)]
        loader = CSVLoader(files=files)
        rows = list(loader.load())

        # TODO: we can verify rows numbers by keys
        assert len(rows) > 0

    for file in valid_csv_files.values():
        verify_single_file(file, file_path_type)

    for file in invalid_csv_files.values():
        with pytest.raises(ValueError):
            verify_single_file(file, file_path_type)


@pytest.mark.parametrize("file_path_type", FILE_PATH_TYPES)
def test_load_multiple_files(valid_csv_files: dict[str, Path], file_path_type: str):
    """
    Test that CSVLoader successfully loads multiple valid CSV files.

    Parametrized to test with 1 or 2 files.
    """

    def verify_multiple_files(files: list[Path | str]):
        loader = CSVLoader(files=files)
        rows = list(loader.load())
        assert len(rows) > 0

    if file_path_type == "str":
        files_to_test: list[str | Path] = [
            str(file) for file in valid_csv_files.values()
        ]
        verify_multiple_files(files_to_test)
    else:
        files_to_test = list(valid_csv_files.values())
        verify_multiple_files(files_to_test)


def test_load_file_not_found():
    """
    Test that CSVLoader raises FileNotFoundError for a non-existent file.
    """
    loader = CSVLoader(files=["/tmp/non_existent_file.csv"])
    with pytest.raises(FileNotFoundError):
        list(loader.load())
