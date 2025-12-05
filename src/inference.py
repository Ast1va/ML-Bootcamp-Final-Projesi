"""Inference helpers for the Online Shoppers project."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Iterable, List

import joblib
import pandas as pd

from src.config import FINAL_MODEL_PATH, SELECTED_FEATURES_PATH


def load_model(model_path: Path = FINAL_MODEL_PATH):
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at {model_path}")
    return joblib.load(model_path)


def load_feature_list(path: Path = SELECTED_FEATURES_PATH) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(f"Feature list not found at {path}")
    with path.open() as f:
        return json.load(f)


def prepare_features(payload: Dict[str, Iterable], feature_order: List[str]) -> pd.DataFrame:
    """Create a one-row DataFrame aligned with training feature order."""
    df = pd.DataFrame([payload])
    df = pd.get_dummies(df, drop_first=True)
    missing_cols = set(feature_order) - set(df.columns)
    for col in missing_cols:
        df[col] = 0
    df = df[feature_order]
    return df


def predict_sample(payload: Dict[str, Iterable],
                   model_path: Path = FINAL_MODEL_PATH,
                   feature_path: Path = SELECTED_FEATURES_PATH):
    model = load_model(model_path)
    features = load_feature_list(feature_path)
    X = prepare_features(payload, features)
    proba = model.predict_proba(X)[0][1]
    pred = model.predict(X)[0]
    return {"prediction": pred, "probability": float(proba)}
