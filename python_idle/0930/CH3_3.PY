import pandas as pd
raw_data = {
    "產品": ["拿鐵", "卡布奇諾", "美式咖啡", "摩卡", "焦糖瑪奇朵"],
    "價格": [120, 130, 100, 150, 160],
    "庫存": [50, 30, 80, 20, 10]
}
df = pd.DataFrame(raw_data)
df.loc[df['產品'] == '美式咖啡', '庫存'] = 120
print(df)
print('=' * 20)
# 設定多重篩選條件
condition = (df['價格'] >= 100) & (df['價格'] <= 150) & (df['庫存'] < 40) #布林遮罩（Boolean Mask）
print(condition)
filtered_df = df[condition] # 語法結構是：新表格 = 舊表格[布林濾網]；只有標記為 True 的橫列會被留下來
print(filtered_df)
