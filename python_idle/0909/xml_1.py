# 引入 Python 內建的 XML 解析模組，並將它簡寫為 ET (這是官方推薦的標準寫法)
import xml.etree.ElementTree as ET

# 定義一個多行字串，內容為標準的 XML 格式資料
# 【結構已調整】：weather_report (此處為最外層根節點) -> city (帶有 name 屬性) -> temp 與 status
xml_data = '''
    <weather_report>
        <city name="台北">
            <temp>30</temp>
            <status>晴</status>
        </city>
    </weather_report>
'''

# ET.fromstring() 的作用是：將「XML 字串」解析成一個 XML「元素物件 (Element Object)」
# 【修正註解】：此處返回的 root 變數，代表著 XML 結構的最外層根節點（也就是 <weather_report>）
root = ET.fromstring(xml_data)

# root.tag 可以取得該節點的「標籤名稱」
# 【修正註解】：因為現在最外層是 <weather_report>，所以這裡會在終端機印出：weather_report
print(root.tag)

# root.findall() 用於尋找所有符合指定路徑的「子節點」
# 【修正註解】：因為目前的 root 變數本身就是 <weather_report>，
# 所以路徑直接寫 'city' 即可（不需要、也不能再寫 weather_report/city，否則會找不到）
# 接著透過 for 迴圈，逐一將找到的每個 <city> 節點暫存到 item 變數中
for item in root.findall('city'):
    
    # item.get('name') 的作用是抓取標籤內部的「屬性（Attribute）」
    # 在 <city name="台北"> 中，name 就是屬性，因此會抓出字串 "台北"
    city_name = item.get('name')
    
    # item.find('temp') 代表在目前的 <city> 節點底下，尋找名為 <temp> 的子節點
    # 後面的 .text 則是關鍵！用來提取該標籤夾在中間的「實際純文字內容」（即 "30"）
    temp = item.find('temp').text
    
    # 同理，在目前的 <city> 節點底下尋找 <status> 子節點，並用 .text 提取其文字內容（即 "晴"）
    status = item.find('status').text
    
    # 將抓取出來的 屬性、溫度文字、天氣狀態文字 一併印出來
    # 終端機輸出結果：台北 30 晴
    print(city_name, temp, status)
