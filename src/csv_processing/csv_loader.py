import csv
from pathlib import Path


class CSVLoader:
    """
    CSV files loader, with path validation.
    """

    def __init__(self, files: list[str | Path]):
        """
        Initialize class with files as list of strings.
        """
        self.files = files

    def load(self, **kwargs):
        """
        Validate CSV files and return generator of rows
        """
        for file in self.files:
            # Auto-convert str to path
            if isinstance(file, str):
                file = Path(file)

            # Verify file exists
            if not file.is_file():
                raise FileNotFoundError(f"File is not found: {file}")

            # Open file and return rows as generator
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile, **kwargs)
                # Get the number of fields from the header
                num_fields = len(reader.fieldnames) if reader.fieldnames else 0
                for i, row in enumerate(reader):
                    # Check if the row has the correct number of fields
                    if len(row) != num_fields:
                        raise ValueError(
                            f"Invalid CSV file detected {file}: row {i} has a different number of fields than the header, expected {num_fields} but got {len(row)}"
                        )
                    yield row
