# 1. 引入內建的 JSON 模組，用於將 Python 物件（如列表、字典）轉換並儲存為 JSON 格式
import json
# 引入內建的 XML 解析模組，並將其簡寫為 ET，用來將實體 XML 檔案解析為元素樹物件
import xml.etree.ElementTree as ET

# 使用 try-except 錯誤捕捉機制，確保當檔案不存在或損毀時，程式能優雅提示而不崩潰
try:
    # 2. 使用 ET.parse() 讀取放置在電腦硬碟中的 'dental.xml' 檔案，建立一個元素樹物件
    tree = ET.parse('dental.xml')
    # 使用 .getroot() 拿到這棵樹的最頂層根節點。以此檔案為例，root 代表的就是總包裝的 <Datas> 標籤
    root = tree.getroot()
    
    # 透過 root.tag 取得根節點的名稱，並使用 f-string 印出系統提示（畫面將顯示 <Datas>）
    print(f"【系統提示】成功讀取 XML 檔案，最外層標籤為：<{root.tag}>")
    print("=" * 50)
    
    # 🌟 核心關鍵步驟一：建立一個空列表（List），準備用來收集迴圈中產生的每一筆診所字典
    clinic_list = []
    
    # 3. 使用 root.findall('Data') 尋找根節點 <Datas> 底下所有名為 <Data> 的直接子節點
    # 透過 for 迴圈，每次將找到的一個 <Data> 區塊（即一間診所的所有欄位）暫存到 item 變數中
    for item in root.findall('Data'):
        
        # --- 安全防錯取值機制（確保欄位缺失時，程式不會因為 None.text 而閃退當機）---
        
        # 尋找 <機構名稱> 標籤。如果存在，用 .text 挖出文字；不存在則回傳預設字串 "無名稱"
        name_node = item.find('機構名稱')
        name = name_node.text if name_node is not None else "無名稱"
        
        # 尋找 <縣市別代碼> 標籤。如果存在，用 .text 挖出文字；不存在則回傳預設字串 "無代碼"
        county_node = item.find('縣市別代碼')
        county_code = county_node.text if county_node is not None else "無代碼"
        
        # 尋找 <行政區域代碼> 標籤。如果存在，用 .text 挖出文字；不存在則回傳預設字串 "無代碼"
        town_node = item.find('行政區域代碼')
        town_code = town_node.text if town_node is not None else "無代碼"
        
        # 尋找 <電話> 標籤。如果存在，用 .text 挖出文字；不存在則回傳預設字串 "無資料"
        phone_node = item.find('電話')
        phone = phone_node.text if phone_node is not None else "無資料"
        
        # 在螢幕上即時印出目前正在處理哪一間診所，作為進度條提示
        print(f"正在處理：{name}")
        
        # 🌟 核心關鍵步驟二：將這一筆診所安全取出的四個變數，打包成一個 Python 字典（Dictionary）結構
        clinic_dict = {
            "機構名稱": name,
            "縣市別代碼": county_code,
            "行政區域代碼": town_code,
            "電話": phone
        }
        
        # 使用 .append() 語法，把剛剛封裝好的「單一診所字典」塞進迴圈外面的「總清單列表」中
        clinic_list.append(clinic_dict)
        
    print("=" * 50)
    # 使用 len() 函數計算列表內部的元素總數，回報總共成功處理了幾筆診所資料
    print(f"【系統提示】所有資料處理完畢，共計 {len(clinic_list)} 筆。")
    print("【系統提示】正在將資料匯出為 JSON 檔案...")
    
    # 🌟 核心關鍵步驟三：定義要產生的實體 JSON 檔案名稱
    output_filename = "dental_output.json"
    
    # 使用 with open() 以「寫入模式 ('w')」與「utf-8 編碼」開啟（或建立）產出的 JSON 檔案
    # 使用 with 語法的好處是程式寫完後會自動安全關閉檔案，釋放記憶體
    with open(output_filename, "w", encoding="utf-8") as f:
        # 使用 json.dump() 將剛剛收集好所有診所的 Python 列表（clinic_list）直接寫入檔案物件（f）中
        # ensure_ascii=False 是繁體中文不變亂碼的關鍵！迫使 Python 直接儲存中文字而非 \u 碼
        # indent=4 會讓產出的 JSON 文字自動換行並縮排 4 個空格，方便人類閱讀與除錯
        json.dump(clinic_list, f, ensure_ascii=False, indent=4)
        
    print(f"【成功】JSON 檔案已順利產生！請查看同目錄下的：{output_filename}")
        
# 錯誤捕捉一：如果電腦裡根本找不到原本的 'dental.xml' 檔案，會執行此區塊
except FileNotFoundError:
    print("【錯誤】找不到 'dental.xml' 檔案，請確認路徑！")
# 錯誤捕捉二：如果 'dental.xml' 檔案存在，但裡面的 XML 語法有嚴重錯誤，會執行此格式損毀提示
except ET.ParseError:
    print("【錯誤】'dental.xml' 格式損毀。")
# 錯誤捕捉三：攔截其他所有可能發生的未知系統錯誤（例如沒有硬碟寫入權限、記憶體不足等）
except Exception as e:
    print(f"【錯誤】發生非預期錯誤：{e}")
