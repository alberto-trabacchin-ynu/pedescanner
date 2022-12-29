from pathlib import Path
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_full_path(record_name: str):
    full_path = Path().absolute() / "datasets" / "jari" / record_name / "車両情報"
    full_path = list(full_path.iterdir())[0]
    return full_path

def get_init_time_format(record_name: str):
    _, date, time = record_name.split("_")
    date = date[0:4] + "-" + date[4:8] + "_"
    time = time[0:4] + "-" + time[4:6] + ".000"
    return (date + time)

def read_vehicle_data(record_name: str, sel_fields=None) -> pd.DataFrame:
    field_names = ["time", "x_vel", "x_accel", "brake_light", "yaw_vel",
                   "y_accel", "steering_ang", "accel_pedal", "brake_pedal"]
    df = pd.read_csv(get_full_path(record_name), header=None, skiprows=2, 
                     names=field_names, usecols=sel_fields, encoding="cp932")
    init_time = get_init_time_format(record_name)
    start_idx = df.index[df["time"] == init_time].to_list()[0]
    df = df.tail(-start_idx)
    df = df.replace(r"^\s*$", np.nan, regex=True)
    df.dropna(inplace=True)
    return df

def plot_data(df: pd.DataFrame, x_field: str, y_fields: str, normalize=True):
    x_vals = df[x_field].to_numpy()
    x_vals = 0.1 * np.arange(0, df.shape[0], 1)
    for field in y_fields:
        y_val = df[field].to_numpy(dtype=float)
        if normalize:
            y_val = y_val / np.max(y_val)
        plt.plot(x_vals, y_val)
    plt.xlabel(x_field)
    plt.ylabel(y_fields)
    plt.show()

if __name__ == "__main__":
    pass