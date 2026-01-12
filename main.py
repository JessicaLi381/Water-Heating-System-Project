import pandas as pd

#constants
C_WATER = 4.189 #j/g°C
MASS_WATER = 1000.0 #g
T_INITIAL = 25.0 #°C

#csv data
df = pd.read_csv('data.csv')

#calculate heat retained and add as new column (q = mcΔT)
df['heat_retained_j'] = MASS_WATER * C_WATER * (df['temp']- T_INITIAL)

print(df)