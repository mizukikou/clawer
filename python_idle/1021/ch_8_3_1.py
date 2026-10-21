from bs4 import BeautifulSoup

# --- 輸入範例一 ---
html_doc_1 = '<a class="btn primary item" href="https://shop.com/item1">購買商品</a>'

# --- 輸入範例二 ---
html_doc_2 = '<a>缺貨中</a>'


def safe_scrape_attributes(html_string, title):
    print(f"--- {title} ---")
    soup = BeautifulSoup(html_string, "html.parser")
    
    # 找出特定 <a> 標籤
    element = soup.find('a')
    
    if element:
        # 1. 提取該標籤內的文字
        text_content = element.get_text(strip=True)
        
        # 2. 提取 href 屬性，若沒有該屬性，請預設為 尚未開放
        url_content = element.get('href', '尚未開放')
        
        # 3. 提取 class 屬性並進行條件判斷與合併
        class_list = element.get('class')
        if class_list:
            # 存在 class 時，將 List 內容合併成用逗號與空格分隔的字串
            class_content = ", ".join(class_list)
        else:
            # 若沒有 class 屬性，則顯示 無類別
            class_content = "無類別"
            
        # 格式化輸出結果
        print(f"文字內容：{text_content}")
        print(f"連結網址：{url_content}")
        print(f"樣式類別：{class_content}")
    else:
        print("找不到 <a> 標籤")
    print()


# 執行測試
safe_scrape_attributes(html_doc_1, "輸出範例一")
safe_scrape_attributes(html_doc_2, "輸出範例二")
