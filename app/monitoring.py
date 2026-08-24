import json
from enum import StrEnum
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, model_validator


class AlertLevel(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Thresholds(BaseModel):
    normal: float = Field(ge=0)
    alert: float = Field(ge=0)
    danger: float = Field(ge=0)
    extreme: float = Field(ge=0)

    @model_validator(mode="after")
    def thresholds_are_ordered(self) -> "Thresholds":
        values = [self.normal, self.alert, self.danger, self.extreme]
        if values != sorted(values):
            raise ValueError("thresholds must be ordered from normal to extreme")
        return self


class MonitoringPoint(BaseModel):
    constituency: str
    point_id: str
    location_name: str
    coordinates: tuple[float, float]
    thresholds_m: Thresholds


class MonitoringConfig(BaseModel):
    project: str
    version: str
    alert_templates: dict[AlertLevel, str]
    monitoring_points: list[MonitoringPoint]

    @model_validator(mode="after")
    def point_ids_are_unique(self) -> "MonitoringConfig":
        point_ids = [point.point_id for point in self.monitoring_points]
        if len(point_ids) != len(set(point_ids)):
            raise ValueError("point_id values must be unique")
        return self


def load_monitoring_config(path: str | Path = "monitoring_config.json") -> MonitoringConfig:
    config_path = Path(path)
    data: dict[str, Any] = json.loads(config_path.read_text(encoding="utf-8"))
    return MonitoringConfig.model_validate(data)


def classify_level(point: MonitoringPoint, water_level_m: float) -> AlertLevel:
    thresholds = point.thresholds_m
    if water_level_m >= thresholds.extreme:
        return AlertLevel.CRITICAL
    if water_level_m >= thresholds.danger:
        return AlertLevel.HIGH
    if water_level_m >= thresholds.alert:
        return AlertLevel.MEDIUM
    return AlertLevel.LOW