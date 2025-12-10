from argparse import ArgumentParser, Namespace
from enum import StrEnum
from tabulate import tabulate

from csv_processing import CSVLoader
from csv_processing import PerformanceReport


class ReportType(StrEnum):
    PERFORMANCE = "performance"


SETTINGS = {"DEFAULT_REPORT": ReportType.PERFORMANCE}


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
    parser.add_argument("--report", default=SETTINGS["DEFAULT_REPORT"])
    return parser.parse_args()


def main():
    """
    CSV processing CLI utility entrypoint.
    """
    # Initialize CLI args
    args = args_init()

    # Load CSV files into generator
    csv_loader = CSVLoader(args.files)
    data_generator = csv_loader.load()

    # Generate report for tabulate
    if args.report == ReportType.PERFORMANCE:
        performance_report = PerformanceReport(data_generator)
    else:
        raise NotImplementedError(f"Report type {args.report} is not implemented")
    table = performance_report.create()

    # Print report to standard output
    output = tabulate(table, headers=performance_report.headers, tablefmt="outline")

    print(output)


if __name__ == "__main__":
    main()
