import csv
from typing import Dict, Tuple


CONVERSION_FACTORS: Dict[str, Tuple[int, int]] = {}


def load_conversion_factors(csv_file_path: str) -> None:
    """Load conversion factors from CSV into memory."""
    global CONVERSION_FACTORS
    with open(csv_file_path, mode="r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                CONVERSION_FACTORS[row[0]] = (10 ** int(row[-2]), 10 ** int(row[-1]))


def lookup_conversion_number_by_id(csv_file_path: str, entity_id: str) -> Tuple[int, int]:
    if not CONVERSION_FACTORS:
        load_conversion_factors(csv_file_path)
    return CONVERSION_FACTORS.get(entity_id, (1, 1))
