from bs4 import BeautifulSoup
html_data = """
<div class="movie-container">
    <div class="movie-item">
        <h3 class="name">  全面啟動 (Inception)   </h3>
        <p class="rating">評分：8.8</p>
        <div class="tags">
            <span>科幻</span><span>懸疑</span><span>動作</span>
        </div>
    </div>
    <div class="movie-item">
        <h3 class="name">  玩具總動員 (Toy Story)   </h3>
        <p class="rating">評分：8.3</p>
        <div class="tags">
            <span>動畫</span><span>冒險</span><span>喜劇</span>
        </div>
    </div>
</div>
"""
soup = BeautifulSoup(html_data, 'html.parser')
movie_dict = {}
movie_items = soup.select(".movie-item")
for item in movie_items:
    name = item.select_one(".name").text.strip()
    rating_text = item.select_one(".rating").text
    rating_num = float(rating_text.replace("評分：", ""))
    tags_list = [span.text for span in item.select(".tags span")]
    movie_dict[name] = {
        'rating': rating_num,
        'tags': tags_list
    }
print(movie_dict)
