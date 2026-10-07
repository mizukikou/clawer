# # 自訂完整 HTML + webview
import pandas as pd
import webview

df = pd.DataFrame({
    "姓名": ["小明", "小華", "小美"],
    "年齡": [20, 25, 22],
    "城市": ["台北", "桃園", "台中"]
})

# DataFrame → HTML table
table_html = df.to_html(
    index=False,
    classes="my-table"
)

html = f"""
<html>
<head>
<style>
    .my-table {{
        border-collapse: collapse;
        width: 100%;
    }}
    .my-table th, .my-table td {{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }}
    .my-table th {{
        background-color: #f2f2f2;
    }}
</style>
</head>
<body>
{table_html}
</body>
</html>
"""

webview.create_window(
    "DataFrame 表格",
    html=html,
    width=600,
    height=400
)

webview.start()