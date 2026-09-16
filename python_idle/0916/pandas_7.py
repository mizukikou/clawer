import pandas as pd

s = "Bob\n"
print(s+' is a doctor')
print(s.strip()+' is a doctor')

df = pd.DataFrame({
    "user": [" Alice ", "Bob\n", "  Charlie  "],
    "email": ["ALICE@gmail.com", "bob@Gmail.com", "CHARLIE@outlook.com"]
})
print(df)
df["user"] = df["user"].str.strip()
df["email"] = df["email"].str.lower().str.strip()
print(df)


