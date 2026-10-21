from bs4 import BeautifulSoup
from urllib.parse import urljoin  # 考卷前半段推薦的最安全網址拼接工具

# 題目提供的輸入範例一 HTML 資料
html_data = """
<div class="news-list">
    <div class="news-card">
        <h2 class="title"><a href="/news/2026-05-01">今日天氣晴朗紫外線偏高</a></h2>
        <span class="date">2026-05-21</span>
    </div>
    <div class="news-card">
        <h2 class="title"><a href="/news/2026-05-02">【突發】國道發生追撞事故</a></h2>
    </div>
</div>
"""

# 定義基礎網址
base_url = "https://example.com"

# 使用 BeautifulSoup 解析 HTML 原始碼
soup = BeautifulSoup(html_data, 'html.parser')

# 5. 建立用來儲存最終結果的「列表套字典」結構
news_list = []

# 1. 使用「容器化選取策略」遍歷每一個新聞卡片 (.news-card)
news_cards = soup.select(".news-card")

for item in news_cards:
    # 2. 提取新聞標題 (利用 .title 內的 a 標籤文字)
    a_tag = item.select_one(".title a")
    title = a_tag.text.strip()
    
    # 3. 提取超連結 (href 屬性) 並與基礎網址進行串接
    # 使用 urljoin 可以自動且完美處理斜線 / 的拼接問題
    relative_url = a_tag.get("href")
    full_url = urljoin(base_url, relative_url)
    
    # 4. 提取發布時間 (.date)
    # 注意：使用三元運算子 (Inline If) 判斷日期標籤是否存在，若找不到則預設顯示 "即時新聞"
    date_tag = item.select_one(".date")
    date = date_tag.text.strip() if date_tag is not None else "即時新聞"
    
    # 將每一則新聞整理成字典，並 append 進入總列表
    news_list.append({
        'title': title,
        'link': full_url,
        'date': date
    })
# 印出最終結果驗證
print(news_list)
