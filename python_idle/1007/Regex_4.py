import re        # 💡 匯入正規表達式模組，用於洗出符合格式的文字
import requests  # 💡 匯入網路請求模組，用來下載網頁原始碼
import sys       # 💡 匯入系統模組，用於發生連線錯誤時中斷程式

# =================================================================
# 步驟 1：設定兆豐銀行矽谷分行的「聯絡我們」專屬內頁網址
# =================================================================
target_url = "https://www.megabank.com.tw/abroad-page/silicon-valley/zh-tw/contact-us"

# 設定模擬瀏覽器的請求標頭 (Headers)，避免被銀行的安全防火牆誤判為惡意攻擊而阻擋
# Mozilla/5.0：歷史遺留的通用開頭字串，用於模擬瀏覽器的請求，避免被網站誤判為爬蟲
# AppleWebKit/537.36：代表瀏覽器背後使用的「網頁渲染引擎」
# (KHTML, like Gecko)：模擬瀏覽器的核心排版引擎，Gecko 是 Firefox 的排版引擎
# • Safari/537.36：因為 Chrome 是基於 Safari 早期核心演變而來的，所以依據標準也必須把 Safari 的相容版本寫在最後面。
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# =================================================================
# 步驟 2：【安全連線機制】下載網頁 HTML 原始碼
# =================================================================
try:
    print(f"🚀 正在連接兆豐銀行海外分行網頁...\n目標 URL: {target_url}")
    # 發送 GET 請求，並設定 timeout=10 秒防止網頁伺服器沒回應時程式無限卡死
    response = requests.get(target_url, headers=headers, timeout=10)
    
    # 檢查網頁狀態碼，如果不是 200 (例如 404 找不到、500 伺服器出錯)，會主動拋出異常跳到 except 區塊
    response.raise_for_status()  # 自動報警機制
    
    # 順利取得網頁的 HTML 純文字原始碼
    html_content = response.text

except requests.exceptions.RequestException as e:
    # 捕捉所有網路連線異常，印出具體原因並終止程式
    print(f"❌ 網路連線或銀行網站要求拒絕！原因: {e}")
    sys.exit()

# =================================================================
# 步驟 3：針對該網頁文字特徵，設計專屬正規表達式 (Regex)
# =================================================================

# 1. 電子郵件比對規則
# 匹配常見的 Email 結構（例如網頁中的 SVB1@megabank.com.tw）
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# 2. 市話與免付費電話比對規則 (針對全形括號與 0800 進行優化)
# （\d{2,3}）➔ 匹配網頁內出現的全形括號與兩到三位區域號碼（如：「（408）」、「（02）」）
# \d{3,4}-\d{4} ➔ 匹配後方有減號連接的電話主體（如：「283-1888」、「2181-1258」）
# | 0800-\d{3}-\d{3} ➔ 利用 OR 槓 (|) 順便捕捉客服免付費電話（如：「0800-016-168」）
phone_pattern = r"（\d{2,3}）\d{3,4}-\d{4}|0800-\d{3}-\d{3}"

# 3. 兩位數分機號碼比對規則 (高階 Lookbehind 斷言寫法)
# (?<=分機) ➔ 向後看斷言。這是一個隱形條件，限定右邊的數字左邊必須緊黏著「分機」這兩個中文字
# \d{2}     ➔ 匹配兩位數數字。因為網頁上的分機為 19、48、12，故限制剛好 2 碼數字
# 💡 這樣寫就能精準避開門牌地址或日期的兩位數，只抓到真正的分機號碼！
extension_pattern = r"(?<=分機)\d{2}"

# =================================================================
# 步驟 4：執行資料擷取與清洗
# =================================================================
print("\n" + "="*40)
print("🎯 兆豐銀行矽谷分行 - 聯絡資料擷取結果")
print("="*40)

# 1. 擷取並列印 Email
emails = re.findall(email_pattern, html_content)
unique_emails = list(set(emails))  # 利用 set() 特性自動剃除網頁中重覆出現的相同 Email
print(f"📬 官方電子郵件 (共 {len(unique_emails)} 筆):")
for email in unique_emails:
    print(f"   - {email}")

# 2. 擷取並列印 電話號碼
phones = re.findall(phone_pattern, html_content)
unique_phones = list(set(phones))  # 去除重複的電話
print(f"📞 聯絡電話/服務專線 (共 {len(unique_phones)} 筆):")
for phone in unique_phones:
    print(f"   - {phone}")

# 3. 擷取並列印 各業務科室分機
extensions = re.findall(extension_pattern, html_content)
unique_extensions = list(set(extensions))  # 去除重複分機
unique_extensions.sort()  # 將分機號碼從小到大排序 (例如 ['12', '19', '48'])

print(f"☎️ 內部業務科室分機 (共 {len(unique_extensions)} 筆):")
print(f"   - 包含分機號碼: {unique_extensions}")
print("="*40)
