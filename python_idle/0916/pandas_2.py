import pandas as pd
import numpy as np

# 1. 定義原始資料清單 (Raw Data List)
# 資料包含三個主要問題：資料重複、價格含有符號($,)、缺失值呈現為字串 "None"
raw_data = [
    {"item": "iPhone 15", "price": "$29,900"},
    {"item": "iPhone 15", "price": "$29,900"},  # 重複資料
    {"item": "iPad Air", "price": "$19,500"},
    {"item": "MacBook", "price": "None"}        # 缺失值字串
]

# 最適合處理 list+dict 結構的資料
# 純字典（無清單）不能用 pd.DataFrame() 直接轉換，因為 Pandas 無法判斷是要當作列還是欄，且缺乏索引。
df = pd.DataFrame(raw_data) 
print("--- 原始資料 ---")
print(df)

print('=' * 20)
# 去除重複資料，預設會保留第一筆，被刪除那一列的索引編號也會跟著消失
df = df.drop_duplicates() 
print("--- 去除重複後 ---")
print(df)

print('=' * 20)
# 重設索引，drop=True 代表丟棄舊的（不連續）索引，重新從 0 開始編號
df = df.reset_index(drop=True) 
print("--- 重設索引後 ---")
print(df)

print('=' * 20)
# 【修正區】價格欄位清洗流程：
# 1. 必須先用 .str.replace() 清除字串內部的 "$" 和 "," 符號（regex=False 代表純文字精確比對）
df["price"] = df["price"].str.replace("$", "", regex=False).str.replace(",", "", regex=False)

# 2. 將字串 "None" 替換為真正的空值。這裡建議使用 np.nan，因為後續轉數字型態 (float64) 對 np.nan 的相容性最好
# 「防禦性程式設計（Defensive Programming）」
# 先手動把明確定義的缺失值（如 "None"、"-"、"null"）轉成 np.nan。接下來，如果 pd.to_numeric 還產生了新的 NaN，就代表那些格子是「非預期的打錯字資料」，方便後續做除錯（Debug）
# 提早轉成 np.nan，可以讓 Pandas 的許多內建函式（如 .isna()、.fillna()、.dropna()）在第一時間就能正確識別哪些是空值，不必等到最後一步轉數字時才發現。
df["price"] = df["price"].replace("None", np.nan)

# 3. 將整欄字串轉換為數值型態。errors="coerce" 代表如果遇到無法轉換的殘留文字，會強制轉為 NaN，避免程式出錯
df["price"] = pd.to_numeric(df["price"], errors="coerce")

print("--- 最終清洗結果 ---")
print(df)

# 檢查清洗後的資料型態，確認 price 已經成功變成 float64 數字
print("\n--- 資料型態檢查 ---")
print(df.dtypes)
# 最後輸出的 dtype: object，是 Pandas 告訴你「這張檢查結果清單（Series）本身」的資料型態，而不是你原本表格內資料的型態。
