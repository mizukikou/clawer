from urllib.parse import urlparse,parse_qs

full_url = "https://www.google.com/search?q=%E7%86%8A%E9%87%8E%E5%8F%A4%E9%81%93&rls=com.microsoft%3Azh-TW%3A&ie=UTF-8&oe=UTF-8&sourceid=ie7&rlz=1I7ADRA_enTW483&fbs=ABfTbFUhNGvvPEUFOvrsPMHwBXgOf1BDPCnJA7T66GFBo7wwhKveeYrgKKfILHkY2xBG4CLixqCG1ENeZxXbOziRleLcZ7VTzNqCcaiNlxqRXg8CNdp-bEFx5pUXlb9okp1n8U1DkFej6YioFRzfDySh_dWTgWC9UOhJF-8pItbOkwiBGR7Y-K70cQjGh8E3HPoqlEfeM5Xn&aep=10&ntc=1&sxsrf=APpeQnvq6_VnqxC22tKHpQDBVxRxN9y_og%3A1792024742896&mstk=AUtExfCkdqbYn2mytBzTv7C0NBGxfkRtHY5OhuqJZsMg4qWTqgLf5oG6AQ1_SBfVdl9guZKPCdhXA-3gyiM3FahnHn49Zc2hcgKW9iVT6QoBmp2dMpSvjmjGmszOxzyq2hSg8opy3yl8wCx7H7KW9D9Ww3DMgJo6vIE_xSB86x1F4-HKzDMCd3JFwB8FxY-8KEuX0K6BbzzWv3DGTfgdyJOM7IbSm8VquwK-RfNpwxY3TkioRzW2y7RGJ_Kb-A&aioh=3&csuir=1&cs=0&lns_mode=cvst&mtid=6yXQavr6FtWlvr0PtJbTiA4&udm=50"

parsed_url = urlparse(full_url)
print("解析後的完整 URL:", parsed_url)  # 中文說明解析後的完整 URL
query_params = parse_qs(parsed_url.query)
print("解析後的查詢參數:", query_params)  # 中文說明解析後的查詢參數
path_url = parsed_url.path
print("解析後的路徑:", path_url)  # 中文說明解析後的路徑
netloc_url = parsed_url.netloc
print("解析後的網域:", netloc_url)  # 中文說明解析後的網域
scheme_url = parsed_url.scheme
print("解析後的協議:", scheme_url)  # 中文說明解析後的協議
fragment_url = parsed_url.fragment
print("解析後的片段:", fragment_url)  # 中文說明解析後的片段
username_url = parsed_url.username
print("解析後的使用者名稱:", username_url)  # 中文說明解析後的使用者名稱
password_url = parsed_url.password
print("解析後的密碼:", password_url)  # 中文說明解析後的密碼
hostname_url = parsed_url.hostname
print("解析後的主機名稱:", hostname_url)  # 中文說明解析後的主機名稱
port_url = parsed_url.port
print("解析後的連接埠:", port_url)  # 中文說明解析後的連接埠
