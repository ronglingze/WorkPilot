"""A deliberately narrow, read-only local CSV tool.

This function is separate from the LLM. It can be tested without an API key.
"""

import csv
from pathlib import Path


CSV_PATH = Path(__file__).resolve().parents[1] / "data" / "sales.csv"


def summarize_sales() -> dict:
    """Read the project sample sales CSV and return total and regional amounts."""
    by_region: dict[str, int] = {}
    with CSV_PATH.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            region = row["region"]
            amount = int(row["amount"])
            by_region[region] = by_region.get(region, 0) + amount
    return {"total": sum(by_region.values()), "by_region": by_region}


if __name__ == "__main__":
    print(summarize_sales())
