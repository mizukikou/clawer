from lxml import etree

# ==============================================================================
# 【測試範例一】
# 結構為：div[@id='main-content'] -> section -> article -> ul -> li
# ==============================================================================
html_str_1 = """
<div id="main-content">
    <section>
        <article>
            <ul>
                <li>Python 爬蟲特訓</li>
                <li>自動化測試實戰</li>
            </ul>
        </article>
    </section>
</div>
"""

print("--- 輸出結果一 ---")
tree_1 = etree.HTML(html_str_1)
# 核心 XPath 語法：不論中間隔了 section/article/ul，直接用 // 跳轉至 li
course_items_1 = tree_1.xpath("//div[@id='main-content']//li/text()")

for item in course_items_1:
    print(f"課程項目：{item}")


print("\n" + "="*40 + "\n")


# ==============================================================================
# 【測試範例二】
# 結構為：div[@id='main-content'] -> div -> ol -> li
# ==============================================================================
html_str_2 = """
<div id="main-content">
    <div>
        <ol>
            <li>Java 基礎教學</li>
        </ol>
    </div>
</div>
"""

print("--- 輸出結果二 ---")
tree_2 = etree.HTML(html_str_2)
# 使用一模一樣的 XPath 語法，同樣能跨越 div/ol 成功抓到資料
course_items_2 = tree_2.xpath("//div[@id='main-content']//li/text()")

for item in course_items_2:
    print(f"課程項目：{item}")
