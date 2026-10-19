from bs4 import BeautifulSoup

# 題目提供的輸入範例一 HTML 資料
html_data = """
<div class="movie-container">
    <div class="movie-item">
        <h3 class="name">  全面啟動 (Inception)   </h3>
        <p class="rating">評分：8.8</p>
        <div class="tags">
            <span>科幻</span><span>懸疑</span><span>動作</span>
        </div>
    </div>
    <div class="movie-item">
        <h3 class="name">  玩具總動員 (Toy Story)   </h3>
        <p class="rating">評分：8.3</p>
        <div class="tags">
            <span>動畫</span><span>冒險</span><span>喜劇</span>
        </div>
    </div>
</div>
"""

# 使用 BeautifulSoup 解析 HTML 原始碼
soup = BeautifulSoup(html_data, 'html.parser')

# 建立用來儲存最終結果的字典
movie_dict = {}

# 1. 找出所有的電影區塊 (.movie-item)
movie_items = soup.select(".movie-item")

for item in movie_items:
    # 2. 提取電影名稱並使用 .strip() 去除兩端多餘的空格與換行
    # 使用 item.select_one 進行局部查找（容器化選取），避免全局陷阱
    name = item.select_one(".name").text.strip()
    
    # 3. 提取電影評分 (.rating)，移除 "評分：" 並轉換為浮點數 (float)
    rating_text = item.select_one(".rating").text
    rating_num = float(rating_text.replace("評分：", ""))
    
    # 4. 使用列表生成式 (List Comprehension) 提取該電影的所有標籤文字
    tags_list = [span.text for span in item.select(".tags span")]
    
    # 5. 整理儲存於字典中，以電影名稱作為 Key，其 Value 包含評分與標籤
    movie_dict[name] = {
        'rating': rating_num,
        'tags': tags_list
    }

# 印出最終結果驗證
print(movie_dict)
