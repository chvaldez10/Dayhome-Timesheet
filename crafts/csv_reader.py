import pandas as pd

TEST_CSV = "2023-12-12.csv"

class CSV_Reader:
    def __init__(self) -> None:
        pass

df = pd.read_csv(TEST_CSV)
print(df.columns)
print(df.loc[:, "Times"])