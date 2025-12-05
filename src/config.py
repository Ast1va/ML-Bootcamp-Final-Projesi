"""Config module with common paths and simple settings templates."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


SRC_DIR = Path(__file__).resolve().parent
BASE_DIR = SRC_DIR.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_PATH = DATA_DIR / "raw" / "online_shoppers_intention.csv"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"
FINAL_MODEL_PATH = MODELS_DIR / "final" / "final_model.pkl"
SELECTED_FEATURES_PATH = MODELS_DIR / "final" / "selected_features.json"
TEMPLATES_DIR = SRC_DIR / "templates"


@dataclass
class TrainingConfig:
    target_column: str = "Revenue"
    test_size: float = 0.2
    random_state: int = 42
    n_estimators: int = 200
    max_depth: Optional[int] = None
    model_path: Path = FINAL_MODEL_PATH
    features_path: Path = SELECTED_FEATURES_PATH
    raw_data_path: Path = RAW_DATA_PATH
    processed_data_dir: Path = PROCESSED_DATA_DIR


@dataclass
class AppConfig:
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True
    template_dir: Path = TEMPLATES_DIR


def ensure_directories() -> None:
    """Create expected folders if they do not exist."""
    for path in [DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, FINAL_MODEL_PATH.parent]:
        path.mkdir(parents=True, exist_ok=True)


__all__ = [
    "SRC_DIR",
    "BASE_DIR",
    "DATA_DIR",
    "RAW_DATA_PATH",
    "PROCESSED_DATA_DIR",
    "MODELS_DIR",
    "FINAL_MODEL_PATH",
    "SELECTED_FEATURES_PATH",
    "TEMPLATES_DIR",
    "TrainingConfig",
    "AppConfig",
    "ensure_directories",
]
