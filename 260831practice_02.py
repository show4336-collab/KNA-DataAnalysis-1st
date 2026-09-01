import pandas as pd

df = pd.read_csv(
    ".venv/01-02_원료_전처리와_제선_제선조업.csv", parse_dates=["timestamp"]
)

before = df.iloc[:360]
after = df.iloc[360:]

cols = ["blast_flow_nm3min", "blast_pressure_kpa", "blower_vib_mms"]

print(before[cols].mean())
print(after[cols].mean())
