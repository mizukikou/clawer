from bs4 import BeautifulSoup

# --- 輸入範例一 ---
html_data_1 = """
<div class="menu">
    <div class="course-group">
        <h2>程式設計</h2>
        <ul>
            <li>Python 入門</li>
            <li>Java 進階實戰</li>
        </ul>
    </div>
    <div class="course-group">
        <h2>網頁前端</h2>
        <ul>
            <li>Vue.js 框架開發</li>
            <li>Bootstrap 網頁美化</li>
        </ul>
    </div>
</div>
"""

# --- 輸入範例二 ---
html_data_2 = """
<div class="menu">
    <div class="course-group">
        <h2>資料科學</h2>
        <ul>
            <li>Pandas 資料分析</li>
            <li>機器學習導論</li>
            <li>深度學習應用</li>
        </ul>
    </div>
</div>
"""


def parse_course_menu(html_string, title_label):
    print(f"--- {title_label} ---")
    soup = BeautifulSoup(html_string, "html.parser")
    
    # 建立一個空字典，用來儲存最終格式 {"分類名": [子項目列表]}
    result_dict = {}
    
    # 核心步驟 1：採用容器化選取策略，撈出所有的課程群組容器
    groups = soup.select('.course-group')
    
    for group in groups:
        # 核心步驟 2：在目前容器內部尋找分類名稱 (h2)
        h2_tag = group.select_one('h2')
        
        if h2_tag:
            category_name = h2_tag.get_text(strip=True)
            
            # 核心步驟 3：運用「列表生成式」快速提取當前群組內所有 li 的純文字
            # 限制在 group 內搜尋 ul li，確保不會撈到其他分類的課程
            courses_list = [li.get_text(strip=True) for li in group.select('ul li')]
            
            # 核心步驟 4：將分類名稱作為 Key，課程列表作為 Value 存入字典
            result_dict[category_name] = courses_list
            
    # 印出最終符合考卷格式的字典結構
    print(result_dict)
    print()


# 執行測試
parse_course_menu(html_data_1, "輸出結果一")
parse_course_menu(html_data_2, "輸出結果二")
