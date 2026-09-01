
## 
##list1 = [10,20,30,40,50]
##print(list1)
##
##
##list1 = [10,10,10]
##list2 = ["00","01","02","03","04","05"],["10","11","12","13","14","15"],["20","21","22","23","24","25"]
##
##print(list2[0][3])
##print(list2[1][2])
##
##import sys
##print(sys.executable)
##
##news_data = [["TSMC股價新高",1500],["AI概念股轉強",800],["美股轉紅",1200]]
##print("第三則新聞：", news_data[2][0])
      
##single_news = { "title":"台積電股價新高", "click":1500,"source":"財經日報"}
##print("新聞標題:",single_news["title"])
##print("新聞來源:",single_news["sources"])  # 找不到時回傳錯誤
##print("新聞來源:",single_news.get["sources"]) # 找不到時回傳 None

##all_news = [
##    {"title": "台積電", "price": 800, "rank": 1},
##    {"title": "聯發科", "price": 1000, "rank": 2},
##    {"title": "鴻海", "price": 150, "rank": 3}
##]

##for item in all_news:
##    print("標題:",item["title"])
##    print("價格:",item["price"])
##    print("排名:",item["rank"])
##    print()
    
##print("標題\t價格\t排名")
##for item in all_news:
##    print(f"{item['title']}\t{item['price']}\t{item['rank']}")

cart = [
    {"name": "Python 書籍", "price": 450, "count": 1},
    {"name": "無線滑鼠", "price": 890, "count": 2},
    {"name": "螢幕支架", "price": 1200, "count": 1}
]

total_cost = 0
for item in cart:
    subtotal = item["price"] * item["count"]
    total_cost += subtotal
    print(f"商品: {item['name']}, 小計: {subtotal}")

print(f"總結帳金額: {total_cost}")



