from pathlib import Path
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_full_path(record_name: str):
    full_path = Path().absolute() / "datasets" / "jari" / record_name / "車両情報"
    full_path = list(full_path.iterdir())[0]
    return full_path

def read_vehicle_data(record_name: str, sel_fields=None) -> pd.DataFrame:
    field_names = ["time", "x_vel", "x_accel", "brake_light", "yaw_vel",
                  "y_accel", "steering_ang", "accel_pedal", "brake_pedal"]
    df = pd.read_csv(get_full_path(record_name), header=None, skiprows=2, 
                     names=field_names, usecols=sel_fields, encoding="cp932")
    #df = df.replace(r"^\s*$", np.nan, regex=True)
    return df

def plot_data(df: pd.DataFrame, x_field: str, y_field: str):
    x_vals = df[x_field].to_numpy()
    x_vals = 0.1 * np.arange(0, 2000, 1)
    y1_vals = df[y_field[0]].to_numpy(dtype=float)
    y1_vals = y1_vals / np.max(y1_vals)
    y2_vals = df[y_field[1]].to_numpy(dtype=float)
    y2_vals = y2_vals / 5
    y3_vals = df[y_field[2]].to_numpy(dtype=float)
    y3_vals = y3_vals / 5
    plt.plot(x_vals, y1_vals)
    plt.plot(x_vals, y2_vals)
    plt.plot(x_vals, y3_vals)
    plt.xlabel(x_field)
    plt.ylabel(y_field)
    plt.show()

if __name__ == "__main__":
    pass