import pandas as pd
df = pd.read_csv("../02_Python_Pandas/cleaned_sales_data.csv")
print("Sales Statistics:")
print(df["Sales"].describe())