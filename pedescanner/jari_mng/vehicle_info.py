from pathlib import Path
import os
import pandas as pd

def read_vehicle_data(record_name: str) -> None:
    full_path = Path().absolute() / "datasets" / "jari" / record_name / "車両情報"
    full_path = list(full_path.iterdir())[0]
    df = pd.read_csv(full_path, encoding="cp932")
    return df

if __name__ == "__main__":
    pass