import logging

from statistics import mean
from collections import defaultdict
from collections.abc import Generator

logger = logging.getLogger(__name__)  # default level is warning


class PerformanceReport:
    """
    A class to generate a performance report from a data generator.
    """

    def __init__(self, data_generator: Generator[dict[str, str], None, None]):
        """
        Initialize the PerformanceReport with a data generator and
        report-specific headers.
        """
        self.data_generator: Generator[dict[str, str], None, None] = data_generator
        self.headers: tuple[str, str] = ("position", "performance")

    def create(self) -> list[tuple[str, float]]:
        """
        Create a sorted performance report from the data generator.
        """
        pos_performances: defaultdict[str, list[float]] = defaultdict(list)

        # Fill total performance per position
        for row in self.data_generator:
            try:
                performance = float(row.get("performance", 0.0))
                pos_performances[row["position"]].append(performance)
            except (KeyError, ValueError) as e:
                logger.warning(f"Skipping row in performance report, {row}: {e}")

        # Calculate average performance for each position
        average_performance = [
            (position, mean(performances))
            for position, performances in pos_performances.items()
            if performances
        ]

        # Return reverse-sorted report by performance field
        return sorted(average_performance, key=lambda x: x[1], reverse=True)
