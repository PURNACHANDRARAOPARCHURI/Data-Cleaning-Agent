import pandas as pd


def compute_metrics(df):
    return {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Missing Values": int(df.isnull().sum().sum()),
        "Duplicate Rows": int(df.duplicated().sum())
    }


def compare_metrics(before, after):
    comparison = {}
    for key in before:
        comparison[key] = {
            "Before": before[key],
            "After": after[key],
            "Improvement": before[key] - after[key]
        }
    return comparison