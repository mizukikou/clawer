from bs4 import BeautifulSoup

# --- 輸入範例一 ---
html_doc_1 = """
<div id="content">
    <h1>    最新消息    </h1>
    <p>發布日期：<span>2026-05-20</span></p>
    <p>    系統已進行升級，感謝您的耐心等候。    </p>
</div>
"""

# --- 輸入範例二 ---
html_doc_2 = """
<div id="content">
    <span>
        特價商品
    </span>
    <strong> $999 </strong>
</div>
"""


def scrape_with_separator(html_string, title):
    print(f"--- {title} ---")
    soup = BeautifulSoup(html_string, "html.parser")
    
    # 1. 定位至 id="content" 的 div 標籤
    content_div = soup.select_one('#content')
    
    if content_div:
        # 2. 利用 .get_text(separator=" | ", strip=True) 
        # 一次完成「插入分隔符」與「清理兩端空白」的任務
        result_text = content_div.get_text(separator=" | ", strip=True)
        
        # 印出結果
        print(result_text)
    else:
        print("找不到指定的區塊")
    print()


# 執行測試
scrape_with_separator(html_doc_1, "輸出範例一")
scrape_with_separator(html_doc_2, "輸出範例二")
