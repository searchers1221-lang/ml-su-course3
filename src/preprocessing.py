"""Общий модуль предобработки (используется в ПР-3, ПР-4, ПР-7)."""
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

TARGET = "price_kusd"
NUM_COLS = ["area_m2", "living_area_m2", "area_sqft", "rooms", "floor",
            "year_built", "dist_center_km"]
CAT_COLS = ["district", "condition", "balcony"]


def clean_raw(df):
    """Правила очистки на основе здравого смысла (не используют статистику выборки,
    поэтому их можно применять ДО разбиения на train/test без утечки)."""
    df = df.drop_duplicates().copy()
    df.loc[df["area_m2"] > 400, "area_m2"] = np.nan                      # квартира > 400 м² — опечатка
    df.loc[~df["year_built"].between(1900, 2026), "year_built"] = np.nan  # невозможный год
    return df


def build_preprocessor(num_cols=NUM_COLS, cat_cols=CAT_COLS):
    num = Pipeline([("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())])
    cat = Pipeline([("imputer", SimpleImputer(strategy="constant", fill_value="неизвестно")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore"))])
    return ColumnTransformer([("num", num, list(num_cols)), ("cat", cat, list(cat_cols))])
