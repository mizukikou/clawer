import os

# 定義正確、健康的 HTML 內容（把原本壞掉的符號換成看得懂的繁體中文）
healthy_html = """
<html eye-strain-reducer="enabled">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
<article class="comment-item">
    <div class="comment-item-header">
        <h3 class="comment-item-header-title">這件衣服穿起來版型超級好看！</h3>
        <span class="comment-item-header-date"><span>2026/10/13</span></span>
    </div>
    <div class="comment-item-fit">
        <p>購買尺寸：M</p>
        <p>尺寸穿起來非常合身，舒適度滿分</p>
    </div>
    <div class="comment-item-subItem comment-item-detail">
        <p>材質摸起來很舒服，出貨速度也很快，非常推薦大家購買，下次還會想回購！</p>
    </div>
    <div class="comment-item-subItem comment-item-info">ThomasKu100 · <span>男生</span> · <span>15~19歲</span></div>
</article>
</body>
</html>
"""

# 組出原本評論範例檔案的絕對路徑
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "評論範例.html")

# 強制用最標準的 utf-8 編碼把這份健康的內容覆蓋進去
with open(html_path, "w", encoding="utf-8") as f:
    f.write(healthy_html)

print("【成功】評論範例.html 已被重置為健康的 UTF-8 繁體中文檔案！")
