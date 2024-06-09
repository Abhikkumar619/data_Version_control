import pandas as pd

Data=[
    {"name": "abishek", "age":22, "city": "mirchaiya"},
    {"name": "rishav", "age":21, "city": "sitapur"},
    {"name": "navin", "age":20, "city": "kanchanpur"},
    {"name": "shambu", "age":32, "city": "mirch"},

]

Data=pd.DataFrame(Data)

Data.to_csv("data/data.csv", index=False)