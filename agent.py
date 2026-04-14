import pandas as pd
import numpy as np


def profile_data(df):
    profile = {}
    for col in df.columns:
        profile[col] = {
            "missing": int(df[col].isnull().sum()),
            "missing_ratio": float(df[col].isnull().mean()),
            "dtype": str(df[col].dtype),
            "unique": int(df[col].nunique())
        }
    return profile


def decide_actions(profile, config):
    decisions = {}

    for col, stats in profile.items():

        if stats["missing_ratio"] > config["drop_threshold"]:
            decisions[col] = ("drop_column", "High missing values")

        elif stats["unique"] <= 1:
            decisions[col] = ("drop_column", "Low variance")

        elif "int" in stats["dtype"] or "float" in stats["dtype"]:
            decisions[col] = ("fill_mean", "Numeric column")

        else:
            decisions[col] = ("fill_mode", "Categorical column")

    return decisions


def handle_outliers(df, logs):
    for col in df.select_dtypes(include=np.number).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        before = ((df[col] < lower) | (df[col] > upper)).sum()

        df[col] = np.where(df[col] < lower, lower, df[col])
        df[col] = np.where(df[col] > upper, upper, df[col])

        after = ((df[col] < lower) | (df[col] > upper)).sum()

        if before > 0:
            logs.append(f"{col}: capped {before} outliers using IQR")

    return df


def apply_actions(df, decisions):
    logs = []

    for col, (action, reason) in decisions.items():

        if col not in df.columns:
            continue

        if action == "drop_column":
            df.drop(columns=[col], inplace=True)

        elif action == "fill_mean":
            df[col].fillna(df[col].mean(), inplace=True)

        elif action == "fill_mode":
            df[col].fillna(df[col].mode()[0], inplace=True)

        logs.append(f"{col}: {action} → {reason}")

    df = handle_outliers(df, logs)

    # Remove duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    removed = before - len(df)

    if removed > 0:
        logs.append(f"Removed {removed} duplicate rows")

    return df, logs