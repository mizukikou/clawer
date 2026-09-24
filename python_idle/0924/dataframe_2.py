import pandas as pd

data = {
      "日期": ["2026-04-13", "2026-04-14", "2026-04-15", "2026-04-16", "2026-04-17"],
      "收盤價": [810, 815, 805, 800, 795],
      "漲跌": [5, 5, -10, -5, -5]
}

df = pd.DataFrame(data)
print(df)

# 練習：顯示股票下跌的收盤價 
# -> Dataframe
df_down = df[df["漲跌"] < 0]
print(df_down)

print(df_down["收盤價"]) # -> Series
print(df_down[["收盤價"]]) # -> Dataframe：外層中括號預期接收「欄位清單」，用「清單」的方式點餐，pandas 就會遵守規則，保持二維表格的容器（DataFrame）來裝它。

df.loc[0:3, ["日期", "收盤價"]] # -> Dataframe：選取前四列的「日期」與「收盤價」欄位，保持二維表格的容器（DataFrame）來裝它。
print(df.loc[0:3, ["日期", "收盤價"]]) 
print(df)
print(df.iloc[1:5, [1, 2]]) # -> Dataframe：選取第2到第5列的第2與第3欄位，因為兩邊指定的都是範圍或清單，所以它會保持二維表格
print(df.iloc[1:5, 1:5]) # 顯示第 2 到第 5 列，第 2 到第 5 欄的資料

# .loc — 依據「名稱/標籤」來找資料
# .iloc — 依據「絕對位置/數字坐標」來找資料（i 代表 Integer）