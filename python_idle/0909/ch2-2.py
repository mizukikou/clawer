import json

# 1. 建立 Python 字典 (包含數字、中文字串、布林值)
my_config = {
    "user_id": 12345,
    "theme": "深色模式",
    "auto_login": True
}

# 2. 轉換為 JSON 字串
# indent=4 達成縮排 4 格
# ensure_ascii=False 達成中文字正常顯示
json_string = json.dumps(my_config, indent=4, ensure_ascii=False)

# 3. 印出結果
print(json_string)
