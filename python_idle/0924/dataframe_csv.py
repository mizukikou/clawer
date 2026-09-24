import pandas as pd
# 設定顯示最大列數為無限，全部印出，只對 DataFrame（二維表格） 有效
pd.set_option('display.max_rows', None) # ）
# 加上這行，將 Series 欄位的最大顯示寬度設為無限
pd.set_option('display.max_colwidth', None)

# 讀取 CSV 檔案並轉換為 DataFrame
# 檔案路徑 G:\我的雲端硬碟\Crawler\課程資料\老師 邵子卿\0924
df = pd.read_csv(r"G:\我的雲端硬碟\Crawler\課程資料\老師 邵子卿\0924\outpatient.csv")
print(df)
# 顯示欄位 roomname & regcount_person
print(df[["roomname", "regcount_person"]])
# 顯示 regcount_person 最大的那整筆資料內容
print('=' * 20)
print(df.loc[df["regcount_person"].idxmax()]) # 顯示 regcount_person 最大的那整筆資料內容，出來是 Serie
# print(df["regcount_person"].max())  # 顯示 regcount_person 的最大值
# print(df.loc[[df["regcount_person"].idxmax()]]) # 顯示 regcount_person 最大的那整筆資料內容，維持 DataFrame 輸出

print(df.iloc[1:5, 1:5]) # 顯示第 2 到第 5 列，第 2 到第 5 欄的資料

print('=' * 20)
# 根據deptname為 板橋_眼科，找出診室和掛號人數
# CSV 原始資料 deptname 欄位有尾隨空白，需先 strip 再比對
print(df.loc[df["deptname"].str.strip() == "板橋_眼科", ["roomname", "regcount_person"]])
# 不使用 loc，分兩步處理：先篩選出所有板橋眼科的橫列(在記憶體中生成一個全新的臨時潛在表格)，再選取所需的欄位
print(df[df["deptname"].str.strip() == "板橋_眼科"][["roomname", "regcount_person"]])