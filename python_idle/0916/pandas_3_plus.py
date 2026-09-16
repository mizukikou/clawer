import json  # 匯入 JSON 模組，用於解析氣象局的 JSON 檔案
import os    # 匯入作業系統路徑模組，用於安全地組合電腦檔案路徑

# ==========================================
# 1. 定義自訂函數：負責解析單一 JSON 檔案並提取溫度
# ==========================================
def extract_temperature(file_object, result_dict):
    """
    功能：讀取已開啟的 JSON 檔案物件，精確切片出該縣市的白天溫度，並直接更新傳入的字典。
    
    【核心優化觀念】：
    因為字典 (dict) 在 Python 中是「可變物件 (Mutable)」，當它被當作參數傳進函數時，
    傳遞的是「記憶體位址」。因此，我們直接在函數內部修改 result_dict，
    外部的 temp_dict 就會同步改變。這裡【不需要】再寫 return 敘述！
    """
    
    # 解析多層樹狀 JSON 結構，將其轉換為 Python 原生字典 (Dict)
    data = json.load(file_object)
    
    # 依據中央氣象署的 JSON 階層，逐層定位到 Location 資料節點
    location_data = data["cwaopendata"]["Dataset"]["Locations"]["Location"]
    
    # 提取縣市名稱（例如："臺東縣"）
    city = location_data["LocationName"]
    
    # 提取包含多行天氣、氣溫、風浪等敘述的天氣描述清單 (List)
    desc_list = location_data["WeatherElement"]["ElementValue"]["WeatherDescription"]
    
    # 準備一個空字串變數，用來存放稍後篩選出來的目標溫度文字
    temp_text = ""
    
    # 遍歷清單中的每一行文字，主動尋找同時包含「氣溫」與「至」的關鍵字行（防禦性寫法）
    for text in desc_list:
        if "氣溫" in text and "至" in text:
            temp_text = text  
            break             # 找到目標文字，立刻中斷並跳出 for 迴圈
            
    # 安全檢查：若檔案內容異常找不到溫度敘述，則印出警告並直接結束函數
    if not temp_text:
        print(f"⚠️ 警告：在【{city}】的資料中找不到任何氣溫相關敘述，自動跳過。")
        return                # 這裡的 return 用來「提早結束函數執行」，不帶任何回傳值

    # 【字串切片邏輯】：利用關鍵字的位置進行前後截取，並用 int() 轉為整數
    # 尋找「溫」字所在的索引位置，並 +1 作為起點
    start = temp_text.index("溫") + 1
    end = temp_text.index("至")
    min_temp = int(temp_text[start:end])
    
    # 尋找「至」字後面一個字元作為最高溫數字的起點
    start = temp_text.index("至") + 1
    end = temp_text.index("度")
    max_temp = int(temp_text[start:end])
    
    # 計算該縣市白天的平均溫度
    avg_temp = (min_temp + max_temp) / 2
    
    # 【關鍵動作】：直接修改記憶體中的字典內容。此動作會直接同步到外部的 temp_dict
    result_dict[city] = avg_temp
    
    # 在終端機即時印出當前檔案的解析進度
    print(f"成功解析【{city}】-> 最低溫：{min_temp}°C | 最高溫：{max_temp}°C | 當日平均：{avg_temp}°C")

    # 💡 註：因為是傳址操作，函數結尾省略了「return result_dict」


# ==========================================
# 2. 主程式執行區 (Main Process)
# ==========================================

# 定義檔案所在的資料夾絕對路徑
base_path = r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20260916"

# 將所有需要批次處理的 JSON 檔案名稱統一收納在一個清單 (List) 中（DRY原則）
file_names = [
    "F-C0032-027.json",
    "F-C0032-026_na.json",
    "F-C0032-018_ch.json",
    "F-C0032-013_i.json",
    "F-C0032-010_nt.json"
]

# 建立一個空字典，這個字典在記憶體中只有一個，稍後會被函數內部直接修改填充
temp_dict = {}

print("=" * 15, "開始批次解析氣象檔案", "=" * 15)

# 使用 for 迴圈，依序將清單中的每一個檔名拿出來處理
for file_name in file_names:
    full_path = os.path.join(base_path, file_name)
    
    try:
        # 以唯讀模式 ('r') 開啟檔案，並指定 utf-8 編碼
        with open(full_path, "r", encoding="utf-8") as td:
            # 呼叫函數。注意：這裡不需要寫「temp_dict = extract_temperature(...)」
            # 只要把 temp_dict 傳進去，它在記憶體中的內容就會被函數直接更新
            extract_temperature(td, temp_dict)
            
    except FileNotFoundError:
        print(f"❌ 錯誤：找不到指定的檔案：{file_name}，系統已自動跳過。")

print("=" * 15, "資料批次解析完成", "=" * 15)


# ==========================================
# 3. 大數據統計與綜合平均值計算
# ==========================================

# 檢查全域字典內是否成功收集到資料（防止除以零的錯誤）
if temp_dict:
    # 💡 技巧：由於 temp_dict 已在迴圈中被函數同步更新，這裡直接取值計算
    total_temp = sum(temp_dict.values())
    average_temp = total_temp / len(temp_dict)
    
    print(f"所有縣市的平均溫度總和  ： {total_temp}°C")
    # 將最終的平均值四捨五入限制到小數點後第兩位
    print(f"所有縣市的平均溫度平均值： {round(average_temp, 2)}°C")
    print("=" * 50)
else:
    print("狀況提示：未成功讀取到任何有效的縣市氣溫資料。")
