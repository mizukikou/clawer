import pandas as pd

df = pd.DataFrame({"title":["新聞A"], "clicks":[100]})
df2 = pd.DataFrame({"title":["新聞B"], "clicks":[150]})
df_concat = pd.concat([df, df2], ignore_index=True)
print(df_concat)

list1 = list(range(1,101))
list2 = []
for i in list1:
    if i % 2 == 0:
        list2.append(i)
        print(list2,end=' ')
print(list2)

# comprehension 推導式/生成式
list3 = [i for i in list1 if i % 2 == 0]
print(list3)

# 任務：透過 dataframe 從 1-100 篩選出偶數
df_numbers = pd.DataFrame({"number": list1})  # 建立包含 1-100 的 dataframe,欄位名稱為 "number"
df_even = df_numbers[df_numbers["number"] % 2 == 0] # 篩選出偶數
df_even = df_even.reset_index(drop=True) # 使用 reset_index 重設索引，drop=True 代表丟棄舊索引
print(f"df_even: \n{df_even}\nShape: {df_even.shape}\nHead: {df_even.head()}\nTail: {df_even.tail()}\nDescribe: {df_even.describe()}\nColumns: {df_even.columns}")
df_even.info()

# df_even.info()幫表格做「全套結構健檢」。會顯示資料表的完整摘要，包含總列數、欄位名稱、有沒有缺失值（Null），以及每個欄位的資料型態。
# df_even.info() 可以快速了解資料表的結構與欄位資訊。
# df_even.columns 可以查看資料表的欄位名稱。
# df_even.describe() 可以查看資料表的統計摘要，包括計數、平均值、標準差、最小值、四分位數和最大值。
# df_even.head() 可以查看資料表的前幾列資料，預設為前五列。
# df_even.tail() 可以查看資料表的後幾列資料，預設為後五列。
# df_even.shape 可以查看資料表的形狀，包括列數和欄位數。
# df_even.reset_index(drop=True) 可以重設索引，drop=True 代表丟棄舊索引。
# df_even["number"].astype(str) 可以將欄位值轉換為字串型態。
# df_even["number"].astype(str).str.strip() 可以去除欄位值的前後空白，通常用於字串欄位。
# df_even.count() 可以計算每個欄位的非缺失值數量。