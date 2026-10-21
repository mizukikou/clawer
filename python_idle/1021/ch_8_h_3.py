# ==============================================================================
# 實作題 3：相簿圖片牆防禦性提取（結合屬性防錯與特殊網址）
# ==============================================================================

import bs4

# 1. 載入題目提供的輸入範例一 HTML 資料
html_data = """
<div class="gallery">
    <div class="gallery-box">
        <span class="photo-title">墾丁美麗海灘</span>
        <img class="preview" src="https://example.com/img/kenting.jpg">
    </div>
    <div class="gallery-box">
        <span class="photo-title">阿里山日出</span>
        <img class="preview"> </div>
    <div class="gallery-box">
        <span class="photo-title">贊助商廣告</span>
    </div>
</div>
"""

# 使用 BeautifulSoup 解析 HTML，建立 DOM 樹狀物件
soup = bs4.BeautifulSoup(html_data, "html.parser")

# 預設的圖片網址變數
default_img = "https://example.com/images/default.jpg"

# ------------------------------------------------------------------------------
# 步驟 1：遍歷相簿內的所有相片格子（容器化選取）
# ------------------------------------------------------------------------------
# 使用 select() 找出所有 class 為 gallery-box 的外層容器大盒子
gallery_boxes = soup.select(".gallery-box")

for item in gallery_boxes:
    # --------------------------------------------------------------------------
    # 步驟 2：提取相片標題（.photo-title）
    # --------------------------------------------------------------------------
    # 限制在當前 item 容器內尋找標題，並用 .text 取得純文字
    title = item.select_one(".photo-title").text
    
    # --------------------------------------------------------------------------
    # 步驟 3 & 4：提取圖片 src 屬性與防錯機制（核心考點）
    # --------------------------------------------------------------------------
    # 提示：先定位 img_tag = item.select_one("img")
    img_tag = item.select_one("img")
    
    # 判斷 img_tag 是否為 None（處理第三個盒子：根本沒有 <img> 標籤的情況）
    if img_tag is not None:
        # 如果 <img> 標籤存在，再使用 .get() 安全提取 "src" 屬性
        # 如果該標籤內沒有寫 src 屬性（處理第二個盒子），則自動給予預設網址
        img_src = img_tag.get("src", default_img)
        
        # 額外防呆：有時 get() 沒給預設值時如果 src 沒寫會回傳 None，
        # 為了確保萬無一失，若 img_src 為 None 則強制指定為預設網址
        if img_src is None:
            img_src = default_img
    else:
        # 如果 img_tag 本身就是 None（完全沒有 <img> 標籤），直接給予預設網址
        img_src = default_img
        
    # --------------------------------------------------------------------------
    # 步驟 5：依序將每張相片的解析結果格式化輸出
    # --------------------------------------------------------------------------
    # 嚴格對齊題目要求的「輸出結果一」格式
    print(f"相片：{title} -> 網址：{img_src}")
