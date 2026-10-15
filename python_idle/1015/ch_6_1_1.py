from urllib.parse import urlparse, parse_qs

def analyze_search_url(url_string):
    """
    解析輸入的網址，提取其搜尋參數並轉換為字典。
    若無參數則回傳 "無參數欄位"。
    """
    # 步驟 1：運用 urlparse() 解析網址
    parsed_url = urlparse(url_string)
    
    # 步驟 2：讀取對應的查詢欄位（即 ? 後方的字串）
    query_string = parsed_url.query
    
    # 步驟 3：安全性與完整性檢查（判斷是否根本「沒有攜帶任何參數」）
    if not query_string:
        return "無參數欄位"
    
    # 步驟 4：運用 parse_qs() 將查詢字串轉為字典
    # 預設會將值 (Value) 包裝成列表 (List)
    result_dict = parse_qs(query_string)
    
    return result_dict


# ==========================================
# 🎯 測試題目提供的範例
# ==========================================

# 測試範例 1：有攜帶多個參數的網址
url1 = "https://www.google.com/search?q=postman&sca_esv=b806ac0cce3d6a6a&rls=com.microsoft%3Azh-TW%3A&rlz=1I7ADRA_enTW483&sxsrf=APpeQnseGIMjTnx5Z244O_ujsgvWG1R3UA%3A1792033826117&fbs=ABfTbFUhNGvvPEUFOvrsPMHwBXgOf1BDPCnJA7T66GFBo7wwhM5svZTbwL96qcNqo9o8OSTgVdu2kShqMetZh8UXJ3eqHDC90dE2zz61hHx1cXxvaF9Au3KOj0I7BUZp0JyguP_Cs_Qu6NTDZ4dBFLOMUix0KbltDH79ACBWJcKi5QN5SbIUlzQ7G54aP_zzp8clvaCG6nN9&vsint=&aep=1&ntc=1&cs=0&sa=X&ved=2ahUKEwjc9oWdhruXAxV0dfUHHSU8F-oQ2J8OegQIHRAD&biw=1745&bih=945&dpr=1.1&mstk=AUtExfDRkH6sLGubExoI39Oy8_BNAHa8A5n4G0DMDbn8SOyhOIOdltGgfMLG4-e4Mk0TTHJKUyWJMDNKg1mtqb2fnUSiwl1d7RaKDdzBZVpMYKOfphh_30MkSIF16bltKBFk4odsDQSsuf8eGwT86M8zTgPFa2AcOtFgDRBWb8_Q9NiRtqCPuaYO-XJTRbmeFh2mN9H0nWzLybBHcTi3JoB5FeTxGrZ22udr4eZlyL03nTVVDNJV6DsbBJSXJg&csuir=1&udm=50m"
output1 = analyze_search_url(url1)
print("輸出範例 1：", output1)
# 預期輸出: {'q': ['postman'], 'sca_esv': ['b806ac0cce3d6a6a'], 'rls': ['com.microsoft%3Azh-TW%3A'], 'rlz': ['1I7ADRA_enTW483'], 'sxsrf': ['APpeQnseGIMjTnx5Z244O_ujsgvWG1R3UA%3A1792033826117'], 'fbs': ['ABfTbFUhNGvvPEUFOvrsPMHwBXgOf1BDPCnJA7T66GFBo7wwhM5svZTbwL96qcNqo9o8OSTgVdu2kShqMetZh8UXJ3eqHDC90dE2zz61hHx1cXxvaF9Au3KOj0I7BUZp0JyguP_Cs_Qu6NTDZ4dBFLOMUix0KbltDH79ACBWJcKi5QN5SbIUlzQ7G54aP_zzp8clvaCG6nN9'], 'vsint': [''], 'aep': ['1'], 'ntc': ['1'], 'cs': ['0'], 'sa': ['X'], 'ved': ['2ahUKEwjc9oWdhruXAxV0dfUHHSU8F-oQ2J8OegQIHRAD'], 'biw': ['1745'], 'bih': ['945'], 'dpr': ['1.1'], 'mstk': ['AUtExfDRkH6sLGubExoI39Oy8_BNAHa8A5n4G0DMDbn8SOyhOIOdltGgfMLG4-e4Mk0TTHJKUyWJMDNKg1mtqb2fnUSiwl1d7RaKDdzBZVpMYKOfphh_30MkSIF16bltKBFk4odsDQSsuf8eGwT86M8zTgPFa2AcOtFgDRBWb8_Q9NiRtqCPuaYO-XJTRbmeFh2mN9H0nWzLybBHcTi3JoB5FeTxGrZ22udr4eZlyL03nTVVDNJV6DsbBJSXJg'], 'csuir': ['1'], 'udm': ['50m']}

# 測試範例 2：完全沒有參數的網址
url2 = "https://example.com"
output2 = analyze_search_url(url2)
print("輸出範例 2：", output2)
# 預期輸出: 無參數欄位
