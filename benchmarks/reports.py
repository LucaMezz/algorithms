"""Export benchmark measurements and summaries."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path

from benchmarks.runner import Measurement, Summary


def write_measurements_csv(path: Path, measurements: list[Measurement]) -> None:
    """Write raw benchmark measurements to CSV."""
    _write_dataclass_csv(path, measurements)


def write_summaries_csv(path: Path, summaries: list[Summary]) -> None:
    """Write aggregated benchmark summaries to CSV."""
    _write_dataclass_csv(path, summaries)


def write_summaries_json(path: Path, summaries: list[Summary]) -> None:
    """Write aggregated benchmark summaries to JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([asdict(summary) for summary in summaries], indent=2),
        encoding="utf-8",
    )


def _write_dataclass_csv(path: Path, rows: list[Measurement] | list[Summary]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return

    fieldnames = list(asdict(rows[0]).keys())
    with path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(asdict(row) for row in rows)

