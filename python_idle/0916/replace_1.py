# raw_data = [
#     {"item": "iPhone 15", "price": "$29,900"},
#     {"item": "iPhone 15", "price": "$29,900"},
#     {"item": "iPad Air", "price": "$19,500"},
#     {"item": "MacBook", "price": "None"} # 缺失值
# ]

# # replace $ and , in the price string
# s= "$29,900"
# print(s.replace("$", "").replace(",", "")) 
# # s.replace("$", "")=29,900。 s.replace("$", "").replace(",", "")=29900

# del_dollars = [data["price"].replace("$", "").replace(",", "") for data in raw_data]
# print(del_dollars)
  
datalist= [10,10,40,40,20,20,30,30]
# 轉換成集合後再轉列表，達到去重效果。因為集合（set）不支援索引操作，透過 list() 函式將這個集合重新包裝
#datalist = list(set(datalist)) #set 是無序的（Unordered），執行後原列表的順序可能會被打亂。
# datalist = list(dict.fromkeys(datalist)) # 利用字典的 Key 不能重複，且會保留順序的特性去重
print(datalist)

print(f"原始的 datalist: {datalist}\n")

# 🛠️ 關鍵修正：使用 datalist.copy() 複製一份一模一樣的清單來跑迴圈
# 這樣外層迴圈會牢牢記住原本的 6 個元素，不會因為內部 remove 縮短清單而導致索引錯亂漏看
for item in datalist.copy():
    
    # ⚠️ 這裡必須在原始 datalist 檢查，因為它正在被動態刪除，計數才會隨之遞減
    count = datalist.count(item)
    print(f"正在檢查 [{item}] -> 目前在清單中剩餘次數: {count}")
    
    # 如果剩餘次數大於 1，代表原始清單中還有多餘的重複值
    if count > 1:
        # 計算需要移除的次數（總次數減 1，表示只留下 1 個，其餘通通刪除）
        remove_times = count - 1
        
        for _ in range(remove_times):
            # .remove() 會由左至右，刪除「第一個」在原始清單中找到的符合元素
            datalist.remove(item)
            
        print(f"   => [處理結果]: 已成功移除多餘的 {item}")

print("\n----------------------------------------")
print(f"最終的 datalist: {datalist}")


list1 = ["A", "B", "C", "D", "E", "s"]
print(list1.index("C")) # 取得 "C" 在 list1 中的索引位置
list2 = "abcdefg"
print(list2.index("c")) # 取得 "c" 在 list2 中的索引位置