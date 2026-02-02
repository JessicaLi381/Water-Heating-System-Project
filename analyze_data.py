import pandas as pd
import numpy as np

# Constants
CP_WATER = 4180.0      # J/(kg°C)
MASS_WATER = 1.0       # kg 
T_AMBIENT = 20.0       # °C

def analyze_data():

    # read the data CSV
    df = pd.read_csv("data.csv")

    # create new column for heat retained in Joules
    df["heat_retained_j"] = MASS_WATER*CP_WATER*(df["temp_C"]-T_AMBIENT)

    # save the processed data
    df.to_csv("processed_data.csv", index=False)

    # summarize findings per material
    summary = (
        df.sort_values("time_min")
            .groupby("material")
            .agg(
                start_temp=("temp_C", "first"),
                final_temp=("temp_C", "last"),
                final_heat_retained=("heat_retained_j", "last"),
                final_time_min=("time_min", "last"),
                cost_cad=("cost_cad","first")
            )
        .reset_index() # turn materials into real columns
    )

    #compute performance per dollar
    summary["performance_per_dollar"] = summary["final_heat_retained"] / summary["cost_cad"]

    #save summary 
    summary.to_csv("summary.csv", index = False)

    #Confirmation
    print("Data process complete.\n\nSummary:\n", summary)


