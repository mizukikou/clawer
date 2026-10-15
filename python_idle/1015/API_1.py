import requests

# 🎯 您找的這串真實 API 非常棒！limit=5 代表只取 5 筆
api_url = "https://fakestoreapi.com/products/category/electronics?limit=5"

# 發送請求
response = requests.get(api_url)

# 將回傳的 JSON 轉成 Python 資料結構
# 💡 註：此時 products 本身就是一個包含 5 個商品字典的「列表 (List)」
products = response.json()

print("=== 🛠️ Fakestore 動態 API 抓取成功 ===")

# 🎯【核心修正】：因為最外層直接就是列表，不需要寫 products['items']
# 我們直接對 products 跑 for 迴圈即可！
for p in products:
    # 🎯【欄位修正】：該 API 定義商品名稱的 Key 是 'title'，不是 'name'
    product_name = p['title']
    product_price = p['price']
    
    print(f"商品：{product_name} | 價格：${product_price}")
