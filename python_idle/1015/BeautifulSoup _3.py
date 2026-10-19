# 任務：從維基百科的Python頁面中提取表格內容並將其換行顯示
import urllib.request  # 標準函式庫：負責發送 HTTP 請求、下載網頁原始碼
import re               # 正規表達式：用來從整頁原始碼中擷取出 <table> 區塊
from bs4 import BeautifulSoup  # 第三方套件：把擷取出來的 HTML 片段解析成可操作的節點樹

# 目標頁面：中文維基百科「Python」條目
url = "https://zh.wikipedia.org/zh-tw/Python"

# 偽裝瀏覽器身分，避免被網站以「非瀏覽器的請求（如直接用程式/爬蟲）」擋下
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# 組成帶有自訂標頭的請求物件（尚未送出）
req = urllib.request.Request(url, headers=headers)

# 送出請求並讀取回應，用 with 讓連線在讀取完後自動關閉
with urllib.request.urlopen(req) as response:
    html_content = response.read().decode("utf-8")  # 回應內容是 bytes，需解碼成字串才能用正規表達式/BeautifulSoup處理
##    print(html_content)

# 用正規表達式從整頁原始碼中，抓出所有 class="wikitable" 的 <table>...</table> 區塊
tables = re.findall(r'(<table class="wikitable">.*?</table>)',  html_content, re.DOTALL)
#  . (點)：代表「任意字元」，不管是英文字母、中文字、數字還是標點符號都算。
#  * (星號)：代表「出現 0 次或無數次」，意思是中間有多少個字都無所謂。
#  ? (問號，非貪婪匹配 ⚠️ 最關鍵)：
# 這是在告訴 Python：「遇到第一個 </table> 就請立刻停下來！」
# 正規表達式中萬用字元 . (點) 雖可匹配任何字，唯獨無法匹配「換行符號（\n）」，加了re.DOTALL 會強行讓 . 擁有跨越換行的超能力。 

print(len(tables))       # 這個頁面總共抓到幾個 wikitable 表格
print("-"*50)
print(tables[0])          # 印出第一個表格的原始 HTML，方便確認擷取是否正確
print("-"*50)

# 使用BeautifulSoup解析提取的表格內容，解析<table>標籤而不是<ul>標籤
# 直接把第一個表格的原始 HTML 丟給 BeautifulSoup 解析（注意：不能先用 re.sub 清掉標籤，
# 否則底下 find("table") 會因為沒有任何標籤而找不到東西）
soup = BeautifulSoup(tables[0], "html.parser")

table_tag = soup.find("table")  # 在解析樹中找到 <table> 節點
print(f"table父節點：{table_tag.parent.name}")  # 因為只丟進單一表格片段，父節點會是最外層的 [document]

# 走訪 <table> 底下的直接子節點（通常只有一個 <tbody>）
for child in table_tag.children:
    if child.name:  # 過濾掉純文字節點（如換行符），只保留有標籤名稱的元素節點
        print(f"table子節點：{child.name}, 內容：{child.text}")