import pandas as pd
import json

df = pd.DataFrame({
    "城市": ["台北", "台中", "高雄"],
    "溫度": [25, 28, 30]
})

# print(df)
# 快速分析：只要一行
# print(f"平均溫度：{round(df['溫度'].mean(),1)} 度")

def extract_temperature(filename):
    data = json.load(filename)
    # print(data)
    #    print("溫度：",data["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
    df = pd.DataFrame(data)
#    print(df)
    city = df["cwaopendata"]["Dataset"]["Locations"]["Location"]["LocationName"]
#    print("溫度：",df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1])
    temp = df["cwaopendata"]["Dataset"]["Locations"]["Location"]["WeatherElement"]["ElementValue"]["WeatherDescription"][1]
    start = temp.index("溫") + 1
    end = temp.index("至")
    min_temp = temp[start:end]
#    print("最低溫度：", min_temp)
    start = temp.index("至") + 1
    end = temp.index("度")
    max_temp = temp[start:end]
#    print("最高溫度：", max_temp)
    avg_temp = (int(min_temp) + int(max_temp)) / 2
#    print("平均溫度：", avg_temp)
    return city,avg_temp

temp_dict = {}
with open(r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20260916\F-C0032-027.json", "r", encoding="utf-8") as td:
    td_city, td_temp = extract_temperature(td)
#    print("縣市：", td_city, "提取的平均溫度：", td_temp)
    temp_dict[td_city] = td_temp

with open(r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20260916\F-C0032-026_na.json", "r", encoding="utf-8") as td:
    na_city, na_temp = extract_temperature(td)
#    print("縣市：", na_city, "提取的平均溫度：", na_temp)
    temp_dict[na_city] = na_temp

with open(r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20260916\F-C0032-018_ch.json", "r", encoding="utf-8") as td:
    ch_city, ch_temp = extract_temperature(td)
#    print("縣市：", ch_city, "提取的平均溫度：", ch_temp)
    temp_dict[ch_city] = ch_temp
    
with open(r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20260916\F-C0032-013_i.json", "r", encoding="utf-8") as td:
    i_city, i_temp = extract_temperature(td)
#    print("縣市：", i_city, "提取的平均溫度：", i_temp)
    temp_dict[i_city] = i_temp
    
with open(r"G:\我的雲端硬碟\Crawler\課程資料\筆記\20260916\F-C0032-010_nt.json", "r", encoding="utf-8") as td:
    nt_city, nt_temp = extract_temperature(td)
#    print("縣市：", nt_city, "提取的平均溫度：", nt_temp)
    temp_dict[nt_city] = nt_temp

print("所有縣市的平均溫度：", temp_dict)

temp_list = 0
for t in temp_dict:
    temp_list += temp_dict[t]
average_temp = temp_list / len(temp_dict)
print("所有縣市的平均溫度總和：", temp_list)
print("所有縣市的平均溫度平均值：", average_temp)
  