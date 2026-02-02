import matplotlib.pyplot as plt
import pandas as pd

#from analyze_data import process_csv, summary_csv
df = pd.read_csv("processed_data.csv")
summary = pd.read_csv("summary_csv")

def plot_cooling_curve():

    for material in sorted(df["material"].unique()):
        material_data = df[df["material"]==material].sort_values("time_min")
        plt.plot(material_data["time_min"], material_data["heat_retained_J"], label=material)
    
    plt.figure()
    plt.title("Heat Retained vs Time (cooling curve)")
    plt.xlabel("Time (min)")
    plt.ylabel("Heat Retained (J)")
    plt.legend()
    plt.show()

def plot_temperature_curve():

    for material in sorted(df["material"].unique()):
        material_data = df[df["material"]==material].sort_values("time_min")
        plt.plot(material_data["time_min"], material_data["temp_C"], label=material)

    plt.figure()
    plt.title("Temperature vs Time")
    plt.xlabel("Time (min)")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.show()

def plot_summary():
    plt.figure()
    plt.title("Summary of Heat Retained by Material")
    plt.xlabel("Material")
    plt.ylabel("Final Heat Retained (J)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()