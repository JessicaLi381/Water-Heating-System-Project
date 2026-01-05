import pandas as pd

data = {
    "Material": ["Towel", "BubbleWrap", "Foam", "Cardboard", "FoilAirGap", "Thermos"], 
    "Cost": [2.00, 1.50, 3.00, 0.75, 1.00, 15.00]
}

df = pd.DataFrame(data, index=["a", "b", "c", "d", "e", "f"])

# add new column
df["initial_temp"] = [60.0, 60.0, 60.0, 60.0, 60.0, 60.0]

# add new row 
new_row = pd.DataFrame([{"Material": "NewMaterial", "Cost": 5.00, "initial_temp": 60.0}], index=["g"])
df = pd.concat([df, new_row])

# add new rows
new_rows = pd.DataFrame([{"Material": "NewMaterial1", "Cost": 5.00, "initial_temp": 60.0},
                         {"Material": "NewMaterial2", "Cost": 6.00, "initial_temp": 60.0}])
df = pd.concat([df, new_rows])

print(df)