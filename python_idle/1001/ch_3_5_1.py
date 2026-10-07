import pandas as pd

# 1. 建立原始資料
dates = ["2026-04-11", "2026-04-12", "2026-04-13"]
df_traffic = pd.DataFrame({"造訪日期": dates})

# 2. 將其轉為時間格式 (pd.to_datetime)
df_traffic["造訪日期"] = pd.to_datetime(df_traffic["造訪日期"])

# 3. 多增加一欄名為 is_weekend，並利用 .dt.weekday >= 5 來判斷
df_traffic["is_weekend"] = df_traffic["造訪日期"].dt.weekday >= 5

# 顯示最終結果
print(df_traffic)
