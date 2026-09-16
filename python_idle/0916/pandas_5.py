import pandas as pd

df1 = pd.DataFrame({"title": ["新聞A"], "clicks": [100]})
print(df1)

df2 = pd.DataFrame({"title": ["新聞B"], "clicks": [150]})
print(df2)
df_combined = pd.concat([df1, df2], ignore_index=True)
print(df_combined)
