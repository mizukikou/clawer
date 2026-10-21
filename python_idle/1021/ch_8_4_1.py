from bs4 import BeautifulSoup

# --- 輸入範例一 ---
html_data_1 = """
<div class="product-list">
    <div class="product-card">
        <h3 class="title">機械鍵盤</h3>
        <span class="price">$2490</span>
        <span class="discount">限時八折</span>
    </div>
    <div class="product-card">
        <h3 class="title">人體工學椅</h3>
        <span class="price">$5200</span>
        <!-- 此商品無折扣標籤 -->
    </div>
</div>
"""

# --- 輸入範例二 ---
html_data_2 = """
<div class="product-list">
    <div class="product-card">
        <h3 class="title">無線滑鼠</h3>
        <span class="price">$1200</span>
        <!-- 此商品無折扣標籤 -->
    </div>
</div>
"""


def parse_products(html_string, title_label):
    print(f"--- {title_label} ---")
    soup = BeautifulSoup(html_string, "html.parser")
    
    # 用來儲存最終所有商品資料的「列表套字典」結構
    product_list = []
    
    # 核心步驟 1：運用「容器化選取策略」，先抓出所有的商品卡片大框框
    cards = soup.select('.product-card')
    
    for card in cards:
        # 核心步驟 2：限制在目前 card 內部進行局部查找
        title_tag = card.select_one('.title')
        price_tag = card.select_one('.price')
        discount_tag = card.select_one('.discount')
        
        # 提取商品名稱
        title = title_tag.get_text(strip=True) if title_tag else ""
        
        # 核心步驟 3：清理價格字串並轉換為整數 (int)
        # 透過 .replace("$", "") 把錢字號拿掉，再用 int() 轉型
        if price_tag:
            price_text = price_tag.get_text(strip=True)
            price = int(price_text.replace("$", ""))
        else:
            price = 0
            
        # 核心步驟 4：運用 Python 三元運算子處理可能缺失的折扣標籤
        discount = discount_tag.get_text(strip=True) if discount_tag else "無折扣"
        
        # 將單一商品的資料整理成字典 (Dictionary)
        item_dict = {
            'title': title,
            'price': price,
            'discount': discount
        }
        
        # 塞入全局列表中
        product_list.append(item_dict)
        
    # 印出最終符合考卷格式的數據結構
    print(product_list)
    print()


# 執行測試
parse_products(html_data_1, "輸出結果一")
parse_products(html_data_2, "輸出結果二")
