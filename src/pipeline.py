"""Training pipeline skeleton for the Online Shoppers project."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Tuple

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from src.config import (
    RAW_DATA_PATH,
    TrainingConfig,
    ensure_directories,
)


def load_data(path: Path) -> pd.DataFrame:
    """Read CSV data from the given path."""
    if not path.exists():
        raise FileNotFoundError(f"Input data not found at {path}")
    return pd.read_csv(path)


def build_dataset(df: pd.DataFrame, target_column: str) -> Tuple[pd.DataFrame, pd.Series]:
    """Split DataFrame into features and target with basic one-hot encoding."""
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not present in data")
    y = df[target_column]
    X = pd.get_dummies(df.drop(columns=[target_column]), drop_first=True)
    return X, y


def train_model(X_train: pd.DataFrame, y_train: pd.Series, config: TrainingConfig) -> RandomForestClassifier:
    """Fit a simple RandomForest classifier."""
    model = RandomForestClassifier(
        n_estimators=config.n_estimators,
        max_depth=config.max_depth,
        random_state=config.random_state,
        n_jobs=-1,
    )
    model.fit(X_train, y_train)
    return model


def evaluate_model(model: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series) -> Dict[str, float]:
    """Return basic evaluation metrics."""
    preds = model.predict(X_test)
    return {
        "accuracy": float(accuracy_score(y_test, preds)),
        "classification_report": classification_report(y_test, preds, output_dict=False),
    }


def save_artifacts(model, feature_columns, config: TrainingConfig) -> None:
    """Persist model and feature names for inference."""
    config.model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, config.model_path)
    with config.features_path.open("w", encoding="utf-8") as f:
        json.dump(list(feature_columns), f, indent=2)


def run_training(config: TrainingConfig = TrainingConfig()) -> Dict[str, float]:
    """Execute the full training flow and return metrics."""
    ensure_directories()
    df = load_data(config.raw_data_path)
    X, y = build_dataset(df, config.target_column)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=config.test_size, random_state=config.random_state, stratify=y
    )
    model = train_model(X_train, y_train, config)
    metrics = evaluate_model(model, X_test, y_test)
    save_artifacts(model, X.columns, config)
    return metrics


if __name__ == "__main__":
    results = run_training()
    print("Training complete. Metrics:")
    for key, value in results.items():
        print(f"- {key}:\n{value}")
