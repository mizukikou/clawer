# ==============================================================================
# 實作題 2：向上尋找所有祖先節點
# 觀念重點：利用 .parents 迭代器與 .name 屬性，由內而外列印出所有長輩標籤
# ==============================================================================

# 引入 Python 的 BeautifulSoup 網頁解析套件
import bs4

# 定義原始碼字串 (題目給予的多層嵌套 HTML 結構)
html_doc = """
<html>
    <body>
        <div id="main_content">
            <section>
                <p>
                    <span id="target">找到我了</span>
                </p>
            </section>
        </div>
    </body>
</html>
"""

# 將 HTML 字串丟入 BeautifulSoup 解析器，建立 DOM 樹狀物件
soup = bs4.BeautifulSoup(html_doc, "html.parser")


# ==============================================================================
# 步驟一：先定位到最深層的目標標籤
# ==============================================================================
# 使用 soup.find() 尋找全網頁中第一個符合標籤名為 "span" 且 id="target" 的元素
target_tag = soup.find("span", id="target")

print(f"目標標籤是：{target_tag}")
# ==============================================================================
# 步驟二與三：使用 .parents 與 for 迴圈依序向上印出標籤名稱
# ==============================================================================
# target_tag.parents 會抓到：<p> -> <section> -> <div> -> <body> -> <html>
# 它是一個迭代器，會由內而外、由近到遠依序釋放出祖先標籤物件

for ancestor in target_tag.parents:
    # ⚠️ 防呆機制：BeautifulSoup 解析到最頂端時，最後一個節點是整個 [document] 物件
    # [document] 物件代表整份文件，它沒有標籤名稱（.name 為 None），必須將它過濾掉
    if ancestor.name is not None:
        
        # ancestor.name 可以取得標籤的名稱（例如：p, section, div...）
        # 依照題目要求的「輸出範例」格式進行標準輸出
        print(f"上層標籤有：{ancestor.name}")
