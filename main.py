from argparse import ArgumentParser, Namespace
from collections import defaultdict
from enum import StrEnum
import csv
from pathlib import Path
from typing import Generator


class ReportType(StrEnum):
    PERFOMANCE = "perfomance"

SETTINGS = {"DEFAULT_REPORT": ReportType.PERFOMANCE}


def args_init() -> Namespace:
    """
    Initialize argument parser with required --files flag(s) and optional
    --report flag to show it
    """
    parser = ArgumentParser(
        prog="csv-processing-demo",
        description="Generate reports from provided CSV files",
    )

    parser.add_argument(
        "--files",
        action="append",
        required=True,
        help="File(s) to process, use multiple `--files` flags if you need to\
                process many files.",
    )
    parser.add_argument("--report", default=SETTINGS["DEFAULT_REPORT"])
    return parser.parse_args()


class CSVLoader:
    """
    CSV files loader, with path validation
    """

    def __init__(self, files: list[str]):
        """
        Initialize class with files as list of strings
        """
        self.files = files

    def load(self):
        """
        Validate CSV files and return generator of rows
        """
        for file in self.files:
            file = Path(file)

            # Verify file exists
            if not file.is_file():
                raise FileNotFoundError(f"File is not found: {file}")

            # Open file and return rows as generator
            try:
                with open(file) as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        yield row
            except csv.Error as e:
                raise ValueError(f"Invalid CSV file detected {file}: {e}") from e

class PerfomanceReport():
    def __init__(self, data_generator: Generator):
        self.data_generator = data_generator

    def create(self):
        results = defaultdict(str)
        for row in self.data_generator:
            if
            print(row.get("position"))
            print(row.get("performance"))



def main():
    # Initialize CLI args
    args = args_init()

    # Load CSV files into generator
    csv_loader = CSVLoader(args.files)
    data_generator = csv_loader.load()

    # Generate report for tabulate
    perfomance_report = PerfomanceReport(data_generator)
    report = perfomance_report.create()


if __name__ == "__main__":
    main()
