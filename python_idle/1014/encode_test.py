import os

# 自動定位到 1014 資料夾
current_dir = os.path.dirname(os.path.abspath(__file__))

# 修正核心：比對正確的開頭 'a05018102'
target_file = None
for filename in os.listdir(current_dir):
    if filename.startswith("a05018102"):
        target_file = filename
        break

if not target_file:
    print("❌ 找不到該檔案。")
else:
    csv_file_path = os.path.join(current_dir, target_file)
    print(f"✨ 成功鎖定真實檔案！真實全名為: '{target_file}'")
    print("=" * 60)

    # --------------------------------------------------------------------------
    # 【實驗 1】嘗試使用傳統的 encoding='utf-8' 讀取
    # --------------------------------------------------------------------------
    print("【實驗 1】嘗試使用 encoding='utf-8' 讀取...")
    try:
        with open(csv_file_path, "r", encoding="utf-8") as f:
            content_utf8 = f.read(300)
        print("💡 讀取成功，但第一個字前面會多出微軟特殊的 \\ufeff 雜訊：")
        print(repr(content_utf8[:100]))
    except UnicodeDecodeError as err:
        print(f"❌ 實驗 1 失敗！噴出解碼錯誤：{err}")

    print("-" * 60)

    # --------------------------------------------------------------------------
    # 【實驗 2】嘗試使用解決微軟 Excel BOM 記號的 encoding='utf-8-sig' 讀取
    # --------------------------------------------------------------------------
    print("【實驗 2】嘗試使用微軟 BOM 救星 encoding='utf-8-sig' 讀取...")
    try:
        with open(csv_file_path, "r", encoding="utf-8-sig") as f:
            content_sig = f.read(300)
        print("✨ 實驗 2 成功解碼！微軟開頭記號被自動削掉了！")
        print("📊 解析出來的前 2 行乾淨資料：")
        lines = content_sig.splitlines()
        for idx, line in enumerate(lines[:2]):
            print(f" ➡️  第 {idx+1} 行: {line}")
    except Exception as err:
        print(f"❌ 實驗 2 失敗：{err}")

    print("-" * 60)

    # --------------------------------------------------------------------------
    # 【實驗 3】嘗試使用選擇題標準答案的傳統編碼 encoding='cp950' 讀取
    # --------------------------------------------------------------------------
    print("【實驗 3】嘗試使用選擇題答案 encoding='cp950' 讀取...")
    try:
        with open(csv_file_path, "r", encoding="cp950") as f:
            content_cp950 = f.read(300)
        print("💡 嘗試用 cp950 讀取結果：")
        print(content_cp950[:100])
    except UnicodeDecodeError as err:
        print(
            f"❌ 實驗 3 失敗！因為這是一支新式 UTF-8 檔案，硬用舊的 cp950 讀取會直接宣告崩潰！"
        )
        print(f"👉 錯誤訊息：{err}")

print("=" * 60)
