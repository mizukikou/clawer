from bs4 import BeautifulSoup

# --- 輸入範例一 ---
html_doc_1 = """
<div>
    <ul class="sidebar"><li>側邊廣告</li></ul>
    <div id="main-content">
        <ul class="goods">
            <li>蘋果筆電</li>
            <li>智慧手錶</li>
            <div>
                <li>深層嵌套的無效項目</li>
            </div>
        </ul>
    </div>
</div>
"""

# --- 輸入範例二 ---
html_doc_2 = """
<div id="main-content">
    <ul class="category">
        <li>微單眼相機</li>
        <li>全幅鏡頭</li>
    </ul>
</div>
<ul class="footer"><li>頁尾免責聲明</li></ul>
"""


def scrape_core_goods(html_string, title):
    print(f"--- {title} ---")
    soup = BeautifulSoup(html_string, "html.parser")

    # 精準定位：先限制在 #main-content 區塊內，再找 ul 的直接子代 li
    results = soup.select('#main-content ul > li')

    # 使用 for 迴圈將商品名稱逐行印出
    for element in results:
        print(f"核心商品：{element.get_text(strip=True)}")
    print()


# 執行測試
scrape_core_goods(html_doc_1, "輸出結果一")
scrape_core_goods(html_doc_2, "輸出結果二")
