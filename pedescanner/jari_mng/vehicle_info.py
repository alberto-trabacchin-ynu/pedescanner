from pathlib import Path
import os
import pandas as pd

def get_full_path(record_name: str):
    full_path = Path().absolute() / "datasets" / "jari" / record_name / "車両情報"
    full_path = list(full_path.iterdir())[0]
    return full_path

def read_vehicle_data(record_name: str, sel_fields=None) -> pd.DataFrame:
    field_names = ["time", "x_vel", "x_accel", "brake_light", "yaw_vel",
                  "y_accel", "steering_ang", "accel_pedal", "brake_pedal"]
    df = pd.read_csv(get_full_path(record_name), header=None, skiprows=1, 
                     names=field_names, usecols=sel_fields, encoding="cp932")
    return df

if __name__ == "__main__":
    pass