from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

import pandas as pd


def _metric_column_name(name: str) -> str:
    """Берёт имя метрики из скобок: 'Relevancy (relevancy)' -> 'relevancy'."""
    match = re.search(r"\(([^()]*)\)", name)
    if match:
        return match.group(1).strip()
    return name.strip()


def _normalize_estimator(estimator: Any, file_path: Path) -> str:
    """Берёт всё только после последнего слеша/обратного слеша."""
    if estimator is None:
        return file_path.parent.name
    return re.split(r"[\\/]", str(estimator))[-1]


def _flatten_metrics(metrics: Any) -> dict[str, Any]:
    """Превращает metrics в плоский словарь с нормализованными названиями."""
    result: dict[str, Any] = {}

    if isinstance(metrics, dict):
        for key, value in metrics.items():
            result[_metric_column_name(str(key))] = value
        return result

    if isinstance(metrics, list):
        for item in metrics:
            if not isinstance(item, dict):
                continue

            metric_name = (
                item.get("name")
                or item.get("metric")
                or item.get("title")
                or item.get("label")
            )
            if metric_name is None:
                continue

            metric_value = item.get("value", item.get("score", item.get("result")))
            result[_metric_column_name(str(metric_name))] = metric_value

    return result


def json_files_to_dataframe(json_files: Iterable[str | Path]) -> pd.DataFrame:
    """Принимает JSON-файлы и возвращает DataFrame с quest, estimator и метриками."""
    rows: list[dict[str, Any]] = []

    for file_name in json_files:
        path = Path(file_name)

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        items = data if isinstance(data, list) else [data]

        for item in items:
            if not isinstance(item, dict):
                continue

            row: dict[str, Any] = {
                "quest": item.get("quest"),
                "estimator": _normalize_estimator(item.get("estimator"), path),
            }
            row.update(_flatten_metrics(item.get("metrics")))
            rows.append(row)

    return pd.DataFrame(rows)

PATH = 'results/estimation/gpt-5.4-automata_v2-delivery_v2/estimated_by_openai/gpt-5.4-mini/gpt-5.4-automata_v2-delivery_v2/'
df = json_files_to_dataframe([PATH + 'quest1_1.json', PATH + 'quest7_1.json', PATH + 'quest10_1.json', PATH + 'quest14_1.json', PATH + 'quest15_1.json'])
