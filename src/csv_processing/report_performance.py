import logging

from collections import defaultdict
from typing import Generator

logger = logging.getLogger(__name__)  # default level is warning


class PerformanceReport:
    def __init__(self, data_generator: Generator):
        self.data_generator = data_generator
        self.headers = ("position", "performance")

    def create(self):
        total_performance = defaultdict(float)
        total_employees = 0

        # Fill total performance per position
        for row in self.data_generator:
            try:
                total_performance[row["position"]] += float(row["performance"])
                total_employees += 1
            except (KeyError, ValueError) as e:
                logger.warning(f"Skipping row in performance report, {row}: {e}")

        # Calculate average performance for each position
        average_performance = [
            (position, format(performance_sum / total_employees, ".2f"))
            for position, performance_sum in total_performance.items()
        ]

        return average_performance

