from app.monitoring import AlertLevel, classify_level, load_monitoring_config


def test_mvp_monitoring_configuration_loads() -> None:
    config = load_monitoring_config()

    assert config.project == "FloodWatch-Ghana"
    assert config.version == "mvp-v1"
    assert len(config.monitoring_points) == 16
    assert config.alert_templates[AlertLevel.CRITICAL] == "flood_emergency"


def test_water_level_is_classified_against_point_thresholds() -> None:
    point = load_monitoring_config().monitoring_points[2]

    assert classify_level(point, 0.9) == AlertLevel.LOW
    assert classify_level(point, 1.2) == AlertLevel.MEDIUM
    assert classify_level(point, 2.0) == AlertLevel.HIGH
    assert classify_level(point, 2.8) == AlertLevel.CRITICAL