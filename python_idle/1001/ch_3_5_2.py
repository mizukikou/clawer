import pandas as pd

# 1. 建立原始訂單資料
order_times = ["08:30", "11:00", "07:15", "13:00"]
df_orders = pd.DataFrame({"訂單時間": order_times})

# 2. 將字串轉為時間格式 (使用 pd.to_timedelta，會自動識別為 時:分:秒)
df_orders["時間格式"] = pd.to_timedelta(df_orders["訂單時間"] + ":00")

# 3. 篩選出所有「早上 9 點以前」的訂單 (小於 9 小時)
#    這裡用 pd.Timedelta('9 hours') 代表早上 9:00 這個時間點
early_birds = df_orders[df_orders["時間格式"] < pd.Timedelta('9 hours')]

# 顯示篩選後的最終結果
print(early_birds)
