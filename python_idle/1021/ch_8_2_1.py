from bs4 import BeautifulSoup

# --- 輸入範例一 ---
html_doc_1 = """
<div class="nav">
    <a class="link active" href="/product/123">旗艦手機 </a>
    <a class="link" href="/product/456">家用電視 </a>
    <a class="link active" href="/news/789">最新消息 </a>
    <a class="link active" href="/product/789">降噪耳機 </a>
</div>
"""

# --- 輸入範例二 ---
html_doc_2 = """
<div class="menu">
    <a class="link active" href="/about">關於我們</a>
    <a class="item active" href="/product/999">精選特價</a>
    <a class="link active" href="/product/001">熱銷排行</a>
</div>
"""


def scrape_products(html_string, title):
    print(f"--- {title} ---")
    soup = BeautifulSoup(html_string, "html.parser")

    # 使用 select() 進行精準的多條件篩選
    # 條件：a 標籤 + .link + .active + [href^="/product"] 屬性開頭
    results = soup.select('a.link.active[href^="/product"]')

    # 依序迭代輸出標籤內的純文字
    for element in results:
        # 使用 .get_text(strip=True) 可以自動修剪掉字串前後的多餘空格
        print(f"篩選結果：{element.get_text(strip=True)}")
    print()


# 執行測試
scrape_products(html_doc_1, "輸出結果一")
scrape_products(html_doc_2, "輸出結果二")
