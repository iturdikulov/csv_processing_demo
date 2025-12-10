from collections.abc import Generator
import csv
from pathlib import Path
from typing import final


@final
class CSVLoader:
    """
    CSV files loader, with path validation.
    """

    def __init__(self, files: list[str | Path]):
        """
        Initialize class with files as list of strings.
        """
        self.files = [Path(f) for f in files]

    def load(self, **kwargs) -> Generator[dict[str, str], None, None]:
        """
        Validate CSV files and return generator of rows.
        """
        for file in self.files:
            # Verify file exists
            if not file.is_file():
                raise FileNotFoundError(f"File is not found: {file}")

            # Open file and return rows as generator
            with open(file, mode="r", newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile, **kwargs)
                fieldnames = reader.fieldnames
                if not fieldnames:
                    raise ValueError(f"CSV file {file} is empty or has no header.")
                num_fields = len(fieldnames)

                for i, row in enumerate(reader):
                    # Check if the row has the correct number of fields
                    # Use actual fieldnames length to compare with row length
                    if len(row) != num_fields:
                        raise ValueError(
                            f"Invalid CSV file detected {file}: row {i + 2} has a different number of fields than the header. "
                            f"Expected {num_fields} but got {len(row)} for row: {row}"
                        )
                    yield row
