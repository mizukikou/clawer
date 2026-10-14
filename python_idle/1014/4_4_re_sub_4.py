import os  # 匯入作業系統模組，用於處理檔案儲存路徑
import re  # 匯入正則表達式模組，用於後續文字排版的微調
import urllib.request as u  # 匯入網路請求模組，並簡寫為 u，用來下載網頁原始碼
from html.parser import HTMLParser  # 從內建庫匯入 HTML 解析器基類


# ==============================================================================
# 核心大腦：客製化 HTML 解析類別
# 繼承 HTMLParser，當 parser.feed() 讀到 HTML 的 <開頭>、</結尾> 或純文字時，會自動觸發對應方法。
# ==============================================================================
class ArticleParser(HTMLParser):
    # 定義一個區塊標籤集合。只要遇到這些標籤，我們就應該換行，避免所有文字擠在同一行。
    BLOCK_TAGS = {
        "br",
        "p",
        "li",
        "tr",
        "table",
        "pre",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
    }

    def __init__(self):
        # 呼叫父類別初始化，convert_charrefs=True 會自動把網頁實體字元（如 &nbsp; 或 &#42;）轉回正常文字
        super().__init__(convert_charrefs=True)
        self.active = False  # 旗標開關：用來標記目前是否正處於維基百科的「文章主體區塊」內
        self.div_depth = 0  # 紀錄 div 的巢狀深度，用來精準判斷主體區塊何時結束
        self.ignore_depth = 0  # 紀錄需要忽略的標籤深度（如遇到 <script> 或 <style> 時）
        self.parts = []  # 收集箱：用來存放所有清洗出來的乾淨純文字片段

    # --------------------------------------------------------------------------
    # 觸發點 A：當解析器讀到任何「開頭標籤」（例如 <div>、<p>、<script>）時
    # --------------------------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)  # 將標籤屬性（原本是元素為 tuple 的 list）轉換成標準字典方便查詢

        # 防線 1：如果目前「還沒進入」主體區塊，就地毯式檢查是不是剛好遇到了核心主體區塊
        if not self.active:
            # 取得該標籤的 class 屬性，若沒有則給空字串，並用空格拆開成清單
            classes = (attrs.get("class") or "").split()
            # 維基百科的正文核心都在 <div class="mw-parser-output"> 內
            # 找出網頁標籤內部的屬性內容是什麼（也就是找出像 mw-parser-output 這樣的暗號）
            # 方法 A 是所有網頁工程師都在用的網頁瀏覽器密技，方法 B 則是利用 Python 程式直接把網頁翻開來看。
            if tag == "div" and "mw-parser-output" in classes:
                self.active = True  # 找到了！開啟儲存開關
                self.div_depth = (
                    1  # 目前 div 深度計數為 1（代表 mw-parser-output 本身）
                )
            return  # 還沒開啟 active 前，底下的過濾邏輯都不執行，直接跳出

        # 防線 2：如果已經進入正文區塊，只要再遇到任何子 <div>，深度計數就 +1
        if tag == "div":
            self.div_depth += 1

        # 防線 3：如果正文區塊內夾雜了網頁腳本 <script> 或樣式表 <style>
        if tag in {"script", "style"}:
            self.ignore_depth += (
                1  # 進入忽略模式（計數 +1），因為我們不想要抓到程式亂碼
            )
            return

        # 如果目前正處於需要忽略的標籤內（ignore_depth > 0），底下的排版與提取直接跳過
        if self.ignore_depth:
            return

        # 排版核心：如果是表格的單元格開頭 <td> 或 <th>，就在文字收集箱裡先塞一個 Tab 鍵 (\t)
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")  # 如果是段落、清單或表格列開頭，先塞一個換行符號 (\n)
        elif tag in {"td", "th"}:
            self.parts.append("\t")

    # --------------------------------------------------------------------------
    # 觸發點 B：當解析器讀到任何「結尾標籤」（例如 </div>、</p>、</script>）時
    # --------------------------------------------------------------------------
    def handle_endtag(self, tag):
        # 如果根本沒進入正文區塊，結尾標籤關我屁事，直接跳出
        if not self.active:
            return

        # 結束忽略模式：如果遇到了 </script> 或 </style> 結尾，忽略計數 -1
        if tag in {"script", "style"} and self.ignore_depth:
            self.ignore_depth -= 1
            return

        # 如果目前還在其他被忽略的區塊深處，直接跳出
        if self.ignore_depth:
            return

        # 排版優化：單元格或區塊結束時，再次適當補上 Tab 或換行，確保資料切齊
        if tag in {"td", "th"}:
            self.parts.append("\t")
        elif tag in self.BLOCK_TAGS:
            self.parts.append("\n")

        # 核心邊界判斷：如果是 </div> 結尾，正文巢狀深度 -1
        if tag == "div":
            self.div_depth -= 1
            # 當深度歸 0 時，代表當初進來的那個 <div class="mw-parser-output"> 已經完全結束了！
            if self.div_depth == 0:
                self.active = (
                    False  # 關閉 active 開關，接下來頁尾的雜訊我們通通不抓了
                )

    # --------------------------------------------------------------------------
    # 觸發點 C：當解析器讀到標籤夾縫中的「純文字資料」時
    # --------------------------------------------------------------------------
    def handle_data(self, data):
        # 只有在 active 為 True（在正文內），且 ignore_depth 為 0（不是網頁程式碼）時，才把文字丟進收集箱
        if self.active and not self.ignore_depth:
            self.parts.append(data)


# ==============================================================================
# 主程式執行流程
# ==============================================================================
url = "https://zh.wikipedia.org/zh-tw/Python"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 Chrome/58.0.3029.110 Safari/537.3"
    )
}

# 打包網路請求，帶上 User-Agent 偽裝成一般瀏覽器，防止被維基百科伺服器拒絕連線
request = u.Request(url, headers=headers)

print("正在連線至 Wikipedia…", flush=True)

try:
    # 發送網路請求，設定 15 秒逾時防卡死
    with u.urlopen(request, timeout=15) as response:
        print(
            f"已收到回應（HTTP {response.status}），正在讀取資料…",
            flush=True,
        )
        # 讀取網頁二進制原始碼，並用 utf-8 解碼成字串，遇到解不出來的字元用 replace 替代防噴錯
        raw_html = response.read().decode("utf-8", errors="replace")

    print("正在解析文章…", flush=True)
    parser = ArticleParser()  # 實例化我們剛剛寫好的 HTML 類別
    parser.feed(raw_html)  # 把好幾萬行的網頁原始碼倒進解析器裡開始清洗
    # .feed() 就是 HTMLParser 老爸傳承下來的，當它嚼著嚼著，發現吞下去的是 <div class="...">，它就會在內部大喊：「報告！我咬到一個開頭標籤了！」，然後自動去呼叫你寫的 handle_starttag()。
    # 當它嚼到 Python - 維基百科 這些純文字時，它又會大喊：「報告！這裡有純文字！」，然後自動去呼叫你寫的 handle_data()。
    
    # --------------------------------------------------------------------------
    # 排版微調部：利用一系列的 Regex 進行連續空格與換行的「修邊壓縮」
    # --------------------------------------------------------------------------
    final_data = "".join(parser.parts)  # 把收集箱裡所有的文字片段組合成一個超大字串

    # 規則 1：把連續 2 次以上的半形空格，壓縮成「單個半形空格」
    final_data = re.sub(r"[ ]+", " ", final_data)

    # 規則 2：如果 Tab 鍵 (\t) 的前後有殘留空格（如 " \t "），全部切齊壓縮成單個 "\t"
    final_data = re.sub(r" *\t+ *", "\t", final_data)

    # 規則 3：如果換行符號 (\n) 的前後有水平空格（如 " \n  "），全部清空，只留下乾淨的換行 "\n"
    final_data = re.sub(r"[ \t]*\n[ \t]*", "\n", final_data)

    # 規則 4：如果段落與段落之間出現了連續 3 次以上的換行（大量空白行），一律壓縮成最多「雙換行（也就是留一個空白行即可）」
    final_data = re.sub(r"\n{3,}", "\n\n", final_data).strip()

    # 安全檢查：如果洗完後發現根本沒文字，代表維基百科可能改版了，拋出例外提示
    if not final_data:
        raise ValueError("找不到文章主體 mw-parser-output") # 直接往下跳到 except Exception as exc:

    # 在終端機印出前功告成的漂亮純文字結果
    print(f"【中文精準清洗完成】:\n{final_data}")

    # --------------------------------------------------------------------------
    # 檔案儲存部：防錯絕對路徑儲存
    # --------------------------------------------------------------------------
    # 自動抓取當前這支 .py 程式在電腦裡的絕對資料夾路徑（不論你在哪裡執行它）
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 把該資料夾路徑與目標檔名結合，組出如 C:\...\1014\4_4_re_sub_4.md 的絕對路徑
    output_path = os.path.join(current_dir, "4_4_re_sub_4.md")

    print(f"正在將結果儲存至 {output_path}…", flush=True)
    # 開啟檔案（'w' 代表覆寫模式），指定 utf-8 編碼確保中文不會變成亂碼
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# Python 維基百科精準清洗結果\n\n")  # 寫入 Markdown 的一級標題
        f.write(final_data)  # 寫入剛剛洗得一乾二淨的精美內文
    print("檔案儲存成功！", flush=True)

except Exception as exc:
    # 只要中間有任何網路斷線、網頁結構對不到或檔案寫入失敗，通通會被這裏抓住並印出錯誤原因
    print(f"抓取或解析失敗：{exc}")
