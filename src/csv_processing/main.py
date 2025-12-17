from argparse import ArgumentParser, Namespace
from enum import StrEnum
from typing import Literal, TypedDict
from tabulate import tabulate

from csv_processing import CSVLoader
from csv_processing import PerformanceReport


class ReportType(StrEnum):
    PERFORMANCE = "performance"


class Settings(TypedDict):
    allowed_reports: list[ReportType]
    # Tabulate support more types, but for us enough this 3 ones
    report_table_format: Literal["plain", "simple", "outline"]
    report_float_format: str


# Global settings
SETTINGS = Settings(
    allowed_reports=[ReportType.PERFORMANCE],
    report_table_format="outline",
    report_float_format=".2f",
)


def args_init() -> Namespace:
    """
    Initialize argument parser with required --files flag(s) and optional
    --report flag to show it.
    """
    parser = ArgumentParser(
        prog="csv-processing-demo",
        description="Generate reports from provided CSV files",
    )

    parser.add_argument(
        "--files",
        action="extend",
        nargs="+",
        required=True,
        help="File(s) to process, use multiple `--files` flags if you need to\
                process many files.",
    )
    parser.add_argument("--report", choices=[SETTINGS.allowed_report])
    return parser.parse_args()


def main():
    """
    CSV processing CLI utility entrypoint.
    """
    args = args_init()

    csv_loader = CSVLoader(args.files)
    data_generator = csv_loader.load()

    performance_report = PerformanceReport(data_generator)
    table = performance_report.create()

    output = tabulate(
        table,
        headers=performance_report.headers,
        tablefmt=SETTINGS.report_table_format,
        floatfmt=SETTINGS.report_float_format,
    )

    print(output)


if __name__ == "__main__":
    main()
